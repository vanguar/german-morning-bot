import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN, MAX_MANUAL_PER_DAY, DEFAULT_LEVEL
from logging_conf import setup_logging
from models import (
    init_db,
    register_user,
    get_user,
    set_level,
    increment_lesson,
    set_last_request,
    increment_manual,
    can_take_manual,
    reset_manual_if_new_day,
    set_last_sent,
    get_progress_text,
    reactivate_if_blocked,
    reset_progress_to_first,
)
from lesson_manager import LessonManager
from utils import utc_date_str

setup_logging()
logger = logging.getLogger(__name__)

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан")

lesson_mgr = LessonManager()

# Клавиатура сразу целиком (aiogram 3)
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📘 Следующий урок")],
        [KeyboardButton(text="🔁 Повторить все")],
        [KeyboardButton(text="📈 Прогресс")],
        [KeyboardButton(text="🏁 Начать с первого урока")],
    ],
    resize_keyboard=True,
)


def build_start_text() -> str:
    return (
        "<b>👋 Привет! Добро пожаловать в мини‑бот ежедневных уроков немецкого.</b>\n\n"
        f"🎯 <b>Уровень по умолчанию:</b> {DEFAULT_LEVEL} (напиши <code>A1</code> или <code>A2</code> чтобы сменить).\n"
        f"🕒 <b>Авто‑урок утром:</b> 1 шт.\n"
        f"⚡ <b>Ручные уроки:</b> до {MAX_MANUAL_PER_DAY} в день (антифлуд отключён).\n\n"
        "🔘 <b>Кнопки:</b>\n"
        "📘 Следующий урок — новый материал\n"
        "🔁 Повторить все — пересмотреть пройденное\n"
        "📈 Прогресс — статистика и %\n"
        "🏁 Начать с первого урока — полный сброс\n\n"
        "ℹ️ Команда: /progress\n"
        "Удачи! 🚀"
    )


# -------- Handlers --------

async def cmd_start(message: Message):
    user_id = message.from_user.id
    register_user(user_id, utc_date_str())
    reactivate_if_blocked(user_id)
    await message.answer(build_start_text(), reply_markup=kb)


async def cmd_progress(message: Message):
    row = get_user(message.from_user.id)
    if not row:
        await message.answer("Сначала /start")
        return
    _, level, lesson_index, *_ = row
    total = lesson_mgr.total(level)
    await message.answer(get_progress_text(message.from_user.id, total))


async def set_level_handler(message: Message):
    new_level = message.text.upper()
    user_id = message.from_user.id
    row = get_user(user_id)
    if not row:
        await message.answer("Сначала /start")
        return
    current_level = row[1]
    if current_level == new_level and row[2] > 0:
        await message.answer(f"Уровень уже {new_level}.")
        return
    set_level(user_id, new_level)
    await message.answer(f"Уровень установлен: {new_level}. Жми «📘 Следующий урок».")  # HTML не нужен


async def repeat_all_handler(message: Message):
    user_id = message.from_user.id
    row = get_user(user_id)
    if not row:
        await message.answer("Сначала /start")
        return

    _, level, lesson_index, *_ = row
    parts = lesson_mgr.repeat_all(level, lesson_index)

    # Если вдруг вернулась одна строка (устаревшие версии),
    # приводим к списку
    if isinstance(parts, str):
        parts = [parts]

    for part in parts:
        await message.answer(part)



async def next_lesson_handler(message: Message):
    user_id = message.from_user.id
    row = get_user(user_id)
    if not row:
        await message.answer("Сначала /start")
        return

    (
        _uid,
        level,
        lesson_index,
        _manual_today,
        _start_date,
        _last_sent,
        _last_req,
        status,
        _reactivated_at,
    ) = row

    if status != "active":
        await message.answer("Статус не active. Напиши /start для реактивации.")
        return

    # Сброс дневного счётчика
    reset_manual_if_new_day(user_id)

    total = lesson_mgr.total(level)
    if lesson_index >= total:
        await message.answer(lesson_mgr.end_message(level))
        return

    # Дневной лимит (если хочешь убрать — вырезай этот блок + increment_manual)
    if not can_take_manual(user_id, MAX_MANUAL_PER_DAY):
        await message.answer("Достигнут лимит ручных уроков на сегодня.")
        return

    text = lesson_mgr.current_or_end(level, lesson_index)
    if not text:
        await message.answer("Не удалось получить урок (проверь lessons.json).")
        return

    await message.answer(text)

    # Обновление прогресса
    set_last_request(user_id)
    increment_lesson(user_id)
    increment_manual(user_id)
    set_last_sent(user_id)


async def restart_from_first_handler(message: Message):
    user_id = message.from_user.id
    row = get_user(user_id)
    if not row:
        register_user(user_id, utc_date_str())

    reset_progress_to_first(user_id)
    row2 = get_user(user_id)
    level = row2[1] if row2 else DEFAULT_LEVEL

    total = lesson_mgr.total(level)
    if total == 0:
        await message.answer("Нет уроков в этом уровне.")
        return

    first_text = lesson_mgr.current_or_end(level, 0)
    await message.answer("<b>Прогресс обнулён.</b> Начинаем сначала!\n\n" + first_text)

    set_last_request(user_id)
    increment_lesson(user_id)
    increment_manual(user_id)
    set_last_sent(user_id)


async def fallback(message: Message):
    await message.answer(
        "Не понял. Кнопки:\n📘 урок • 🔁 повтор • 📈 прогресс • 🏁 сначала\nИли /progress."
    )


# -------- Main --------

async def main():
    init_db()
    dp = Dispatcher()

    dp.message.register(cmd_start, Command("start"))
    dp.message.register(cmd_progress, Command("progress"))
    dp.message.register(set_level_handler, F.text.in_({"A1", "A2", "a1", "a2"}))
    dp.message.register(next_lesson_handler, F.text == "📘 Следующий урок")
    dp.message.register(repeat_all_handler, F.text == "🔁 Повторить все")
    dp.message.register(cmd_progress, F.text == "📈 Прогресс")
    dp.message.register(restart_from_first_handler, F.text == "🏁 Начать с первого урока")
    dp.message.register(fallback)

    bot = Bot(
        BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    logger.info("Bot started (polling)...")
    await dp.start_polling(bot, allowed_updates=["message"])


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Остановлено пользователем.")
