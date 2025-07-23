import asyncio
import os
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN, MAX_MANUAL_PER_DAY, DEFAULT_LEVEL, DB_PATH
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

# Админ-панель клавиатура
admin_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="📊 Статистика за сегодня", callback_data="stats_today"),
        InlineKeyboardButton(text="📈 За неделю", callback_data="stats_week")
    ],
    [
        InlineKeyboardButton(text="📅 За месяц", callback_data="stats_month"),
        InlineKeyboardButton(text="📋 За весь период", callback_data="stats_all")
    ],
    [
        InlineKeyboardButton(text="💾 Скачать базу SQLite", callback_data="download_db"),
        InlineKeyboardButton(text="📄 Экспорт в TXT", callback_data="export_txt")
    ],
    [
        InlineKeyboardButton(text="📊 Экспорт в CSV", callback_data="export_csv")
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
    username = message.from_user.username
    full_name = f"{message.from_user.first_name or ''} {message.from_user.last_name or ''}".strip()
    register_user(user_id, utc_date_str(), username, full_name)
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
        username = message.from_user.username
        full_name = f"{message.from_user.first_name or ''} {message.from_user.last_name or ''}".strip()
        register_user(user_id, utc_date_str(), username, full_name)

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

async def cmd_backup_db(message: Message):
    try:
        from aiogram.types import FSInputFile
        
        # Отправь файл базы
        db_file = FSInputFile(DB_PATH, filename="users_backup.db")
        await message.answer_document(
            db_file,
            caption=f"📁 Резервная копия базы данных\n📅 {utc_date_str()}\n💾 Размер: {os.path.getsize(DB_PATH)} байт"
        )
        
    except Exception as e:
        await message.answer(f"❌ Ошибка: {str(e)}")

# -------- НОВЫЕ АДМИН ФУНКЦИИ --------

async def cmd_admin(message: Message):
    await message.answer(
        "🔧 <b>Админ-панель</b>\n\n"
        "Выберите действие:",
        reply_markup=admin_kb
    )

async def admin_callback_handler(callback: CallbackQuery):
    action = callback.data
    
    if action == "stats_today":
        await show_stats(callback, "today")
    elif action == "stats_week":
        await show_stats(callback, "week")
    elif action == "stats_month":
        await show_stats(callback, "month")
    elif action == "stats_all":
        await show_stats(callback, "all")
    elif action == "download_db":
        await download_database(callback)
    elif action == "export_txt":
        await export_users_txt(callback)
    elif action == "export_csv":
        await export_users_csv(callback)

async def show_stats(callback: CallbackQuery, period: str):
    try:
        from models import get_conn
        import time
        from datetime import datetime, timedelta
        
        now = datetime.now()
        
        # Определяем период
        if period == "today":
            start_date = now.replace(hour=0, minute=0, second=0, microsecond=0)
            title = "📊 Статистика за сегодня"
        elif period == "week":
            start_date = now - timedelta(days=7)
            title = "📈 Статистика за неделю"
        elif period == "month":
            start_date = now - timedelta(days=30)
            title = "📅 Статистика за месяц"
        else:  # all
            start_date = datetime(2020, 1, 1)  # Очень старая дата
            title = "📋 Статистика за весь период"
        
        start_timestamp = int(start_date.timestamp())
        
        with get_conn() as conn:
            cursor = conn.cursor()
            
            # Общее количество пользователей
            cursor.execute("SELECT COUNT(*) FROM users")
            total_users = cursor.fetchone()[0]
            
            # Новые пользователи за период
            cursor.execute("""
                SELECT COUNT(*) FROM users 
                WHERE last_request_at >= ? OR start_date >= ?
            """, (start_timestamp, start_date.strftime('%Y-%m-%d')))
            new_users = cursor.fetchone()[0]
            
            # Активные пользователи за период
            cursor.execute("""
                SELECT COUNT(*) FROM users 
                WHERE last_request_at >= ? AND status = 'active'
            """, (start_timestamp,))
            active_users = cursor.fetchone()[0]
            
            # Статистика по уровням
            cursor.execute("""
                SELECT level, COUNT(*) FROM users 
                WHERE (last_request_at >= ? OR start_date >= ?) AND status = 'active'
                GROUP BY level
            """, (start_timestamp, start_date.strftime('%Y-%m-%d')))
            level_stats = cursor.fetchall()
            
            # Средний прогресс
            cursor.execute("""
                SELECT AVG(lesson_index) FROM users 
                WHERE (last_request_at >= ? OR start_date >= ?) AND status = 'active'
            """, (start_timestamp, start_date.strftime('%Y-%m-%d')))
            avg_progress = cursor.fetchone()[0] or 0
        
        # Формируем сообщение
        stats_text = [
            f"<b>{title}</b>",
            "",
            f"👥 Всего пользователей: <b>{total_users}</b>",
            f"🆕 Новых за период: <b>{new_users}</b>",
            f"🟢 Активных за период: <b>{active_users}</b>",
            f"📚 Средний прогресс: <b>{avg_progress:.1f}</b> урока",
            "",
            "<b>📊 По уровням:</b>"
        ]
        
        for level, count in level_stats:
            stats_text.append(f"  • {level}: <b>{count}</b> чел.")
        
        await callback.message.edit_text(
            "\n".join(stats_text),
            reply_markup=admin_kb
        )
        await callback.answer()
        
    except Exception as e:
        await callback.answer(f"❌ Ошибка: {str(e)}", show_alert=True)

async def download_database(callback: CallbackQuery):
    try:
        from aiogram.types import FSInputFile
        
        db_file = FSInputFile(DB_PATH, filename="users_backup.db")
        await callback.message.answer_document(
            db_file,
            caption=f"📁 База данных SQLite\n📅 {utc_date_str()}"
        )
        await callback.answer("✅ База отправлена!")
    except Exception as e:
        await callback.answer(f"❌ Ошибка: {str(e)}", show_alert=True)

async def export_users_txt(callback: CallbackQuery):
    try:
        from models import get_conn
        from aiogram.types import BufferedInputFile
        
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT user_id, username, full_name, level, lesson_index, start_date, status 
                FROM users ORDER BY user_id
            """)
            users = cursor.fetchall()
        
        text_lines = [
            f"📊 Экспорт пользователей - {utc_date_str()}",
            f"Всего: {len(users)} пользователей",
            "",
            "ID | Username | Имя | Уровень | Урок | Дата старта | Статус",
            "-" * 70
        ]
        
        for user in users:
            user_id, username, full_name, level, lesson_idx, start_date, status = user
            username_display = f"@{username}" if username else "—"
            full_name_display = full_name if full_name else "—"
            text_lines.append(f"{user_id} | {username_display} | {full_name_display} | {level} | {lesson_idx} | {start_date} | {status}")
        
        text_file = BufferedInputFile(
            "\n".join(text_lines).encode('utf-8'),
            filename=f"users_{utc_date_str()}.txt"
        )
        
        await callback.message.answer_document(
            text_file,
            caption=f"📄 Экспорт в TXT\n👥 {len(users)} пользователей"
        )
        await callback.answer("✅ TXT файл отправлен!")
    except Exception as e:
        await callback.answer(f"❌ Ошибка: {str(e)}", show_alert=True)

async def export_users_csv(callback: CallbackQuery):
    try:
        from models import get_conn
        from aiogram.types import BufferedInputFile
        
        with get_conn() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT user_id, level, lesson_index, manual_lessons_today,
                       start_date, last_sent_lesson_at, last_request_at, status 
                FROM users ORDER BY user_id
            """)
            users = cursor.fetchall()
        
        # CSV формат
        csv_lines = [
            "user_id,level,lesson_index,manual_today,start_date,last_sent,last_request,status"
        ]
        
        for user in users:
            csv_lines.append(",".join([str(field) if field is not None else "" for field in user]))
        
        csv_content = "\n".join(csv_lines)
        csv_file = BufferedInputFile(
            csv_content.encode('utf-8'),
            filename=f"users_export_{utc_date_str()}.csv"
        )
        
        await callback.message.answer_document(
            csv_file,
            caption=f"📊 Экспорт в CSV\n👥 {len(users)} пользователей\n💡 Можно открыть в Excel"
        )
        await callback.answer("✅ CSV файл отправлен!")
    except Exception as e:
        await callback.answer(f"❌ Ошибка: {str(e)}", show_alert=True)

# -------- Main --------

async def main():
    init_db()
    dp = Dispatcher()

    dp.message.register(cmd_start, Command("start"))
    dp.callback_query.register(set_level_callback_handler, F.data.startswith("set_level:"))
    
    dp.message.register(cmd_progress, Command("progress"))
    dp.message.register(cmd_backup_db, Command("backup"))
    dp.message.register(cmd_admin, Command("admin"))
    dp.callback_query.register(admin_callback_handler, F.data.startswith(("stats_", "download_", "export_")))
    
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
    logger.info("Scheduler started for daily lessons at 08:00 Europe/Berlin")

    logger.info("Bot started (polling)...")
    await dp.start_polling(bot, allowed_updates=["message", "callback_query"])

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🛑 Остановлено пользователем.")