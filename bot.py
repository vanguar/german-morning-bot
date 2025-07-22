import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN, MAX_MANUAL_PER_DAY, DEFAULT_LEVEL
from logging_conf import setup_logging

# Scheduler imports
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from daily_send import broadcast

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

# Initialize logging
setup_logging()
logger = logging.getLogger(__name__)

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN не задан")

lesson_mgr = LessonManager()

# Основная клавиатура с кнопками навигации по урокам
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📘 Следующий урок")],
        [KeyboardButton(text="🔁 Повторить все"), KeyboardButton(text="📈 Прогресс")],
        [KeyboardButton(text="🏁 Начать с первого урока")],
    ],
    resize_keyboard=True,
)

# Inline-клавиатура для выбора уровня
level_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🚀 Уровень A1", callback_data="set_level:A1"),
        InlineKeyboardButton(text="🚀🚀 Уровень A2", callback_data="set_level:A2")
    ]
])

# Универсальное приветственное сообщение
def build_start_text() -> str:
    return (
        "<b>👋 Привет! Добро пожаловать в мини-бот для изучения 🇩🇪 немецкого.</b>\n\n"
        "Я уже отправил вам первый урок и активировал ежедневную утреннюю рассылку.\n\n"
        "Используйте кнопки ниже для навигации по урокам или смены уровня 👇"
    )

# -------- Handlers --------

async def cmd_start(message: Message):
    user_id = message.from_user.id
    register_user(user_id, utc_date_str())
    reactivate_if_blocked(user_id)
    await message.answer(build_start_text(), reply_markup=level_kb)
    await message.answer("Главное меню:", reply_markup=kb)

    row = get_user(user_id)
    level = row[1]
    first_text = lesson_mgr.current_or_end(level, 0)
    await message.answer(f"<b>🌅 Ваш первый урок</b>\n\n{first_text}")
    set_last_request(user_id)
    increment_lesson(user_id)
    increment_manual(user_id)
    set_last_sent(user_id)
    await message.answer(
        "🔔 Ежедневная утренняя рассылка активирована!\n"
        "Каждое утро вы будете получать новый урок."
    )

async def set_level_callback_handler(callback: CallbackQuery):
    new_level = callback.data.split(":")[1]
    user_id = callback.from_user.id

    row = get_user(user_id)
    if not row:
        await callback.answer("Сначала /start", show_alert=True)
        return

    current_level = row[1]
    if current_level == new_level and row[2] > 0:
        await callback.answer(f"Уровень {new_level} уже активен.", show_alert=True)
        return

    set_level(user_id, new_level)
    await callback.answer(f"Уровень {new_level} установлен!", show_alert=True)
    await callback.message.answer(
        f"✅ Уровень изменён на <b>{new_level}</b>.\n"
        "Нажмите «📘 Следующий урок», чтобы получить новый урок по выбранному уровню."
    )

async def cmd_progress(message: Message):
    row = get_user(message.from_user.id)
    if not row:
        await message.answer("Сначала /start")
        return
    _, level, lesson_index, *_ = row
    total = lesson_mgr.total(level)
    await message.answer(get_progress_text(message.from_user.id, total))

async def repeat_all_handler(message: Message):
    user_id = message.from_user.id
    row = get_user(user_id)
    if not row:
        await message.answer("Сначала /start")
        return

    _, level, lesson_index, *_ = row
    parts = lesson_mgr.repeat_all(level, lesson_index)

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
        _uid, level, lesson_index, _manual_today, _start_date,
        _last_sent, _last_req, status, _reactivated_at,
    ) = row

    if status != "active":
        await message.answer("Статус не active. Напиши /start для реактивации.")
        return

    reset_manual_if_new_day(user_id)
    total = lesson_mgr.total(level)
    if lesson_index >= total:
        await message.answer(lesson_mgr.end_message(level))
        return

    if not can_take_manual(user_id, MAX_MANUAL_PER_DAY):
        await message.answer("Достигнут лимит ручных уроков на сегодня.")
        return

    text = lesson_mgr.current_or_end(level, lesson_index)
    if not text:
        await message.answer("Не удалось получить урок (проверь lessons.json).")
        return

    await message.answer(text)

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
        "Не понял. Кнопки:\n📘 урок • 🔁 повтор • 📈 прогресс • 🏁 сначала\nИли выберите уровень через /start."
    )

# -------- Main --------

async def main():
    init_db()
    dp = Dispatcher()

    dp.message.register(cmd_start, Command("start"))
    dp.callback_query.register(set_level_callback_handler, F.data.startswith("set_level:"))
    
    dp.message.register(cmd_progress, Command("progress"))
    dp.message.register(next_lesson_handler, F.text == "📘 Следующий урок")
    dp.message.register(repeat_all_handler, F.text == "🔁 Повторить все")
    dp.message.register(cmd_progress, F.text == "📈 Прогресс")
    dp.message.register(restart_from_first_handler, F.text == "🏁 Начать с первого урока")
    dp.message.register(fallback)

    bot = Bot(
        BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    # вместо CronTrigger импортируем IntervalTrigger
    scheduler = AsyncIOScheduler(timezone="Europe/Berlin")
    scheduler.add_job(
        broadcast,
        CronTrigger(hour=8, minute=0)
    )

    scheduler.start()
    logger.info("Scheduler started for daily lessons at 08:00 Europe/Berlin")

    logger.info("Bot started (polling)...")
    await dp.start_polling(bot, allowed_updates=["message", "callback_query"])

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Остановлено пользователем.")
