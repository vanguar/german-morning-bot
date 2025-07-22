import sqlite3
import time
from typing import Optional, List, Tuple
from config import DEFAULT_LEVEL


DB_PATH = 'users.db'


def get_conn():
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_conn() as conn:
        c = conn.cursor()
        # ВАЖНО: убрали параметр ?, подставили DEFAULT_LEVEL прямо в SQL
        c.execute(f"""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            level TEXT DEFAULT '{DEFAULT_LEVEL}',
            lesson_index INTEGER DEFAULT 0,
            manual_lessons_today INTEGER DEFAULT 0,
            start_date TEXT,
            last_sent_lesson_at INTEGER,
            last_request_at INTEGER,
            status TEXT DEFAULT 'active',
            reactivated_at INTEGER
        )
        """)
        c.execute("""
        CREATE TABLE IF NOT EXISTS user_errors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            level TEXT,
            lesson_index INTEGER,
            token TEXT,
            error_type TEXT,
            created_at INTEGER
        )
        """)
        conn.commit()


def register_user(user_id: int, start_date: str):
    with get_conn() as conn:
        c = conn.cursor()
        c.execute("""
            INSERT OR IGNORE INTO users (user_id, start_date)
            VALUES (?, ?)
        """, (user_id, start_date))
        conn.commit()


def get_user(user_id: int) -> Optional[Tuple]:
    with get_conn() as conn:
        c = conn.cursor()
        c.execute("""SELECT user_id, level, lesson_index, manual_lessons_today,
                            start_date, last_sent_lesson_at, last_request_at,
                            status, reactivated_at
                     FROM users WHERE user_id=?""", (user_id,))
        return c.fetchone()


def get_active_users() -> List[int]:
    with get_conn() as conn:
        c = conn.cursor()
        c.execute("SELECT user_id FROM users WHERE status='active'")
        return [r[0] for r in c.fetchall()]


def set_level(user_id: int, level: str):
    with get_conn() as conn:
        c = conn.cursor()
        c.execute(
            "UPDATE users SET level=?, lesson_index=0, manual_lessons_today=0 WHERE user_id=?",
            (level, user_id)
        )
        conn.commit()


def reset_progress_to_first(user_id: int):
    """
    Сброс прогресса на первый урок и обнуление дневного счётчика.
    """
    with get_conn() as conn:
        c = conn.cursor()
        c.execute(
            "UPDATE users SET lesson_index=0, manual_lessons_today=0 WHERE user_id=?",
            (user_id,)
        )
        conn.commit()


def increment_lesson(user_id: int):
    with get_conn() as conn:
        c = conn.cursor()
        c.execute("UPDATE users SET lesson_index = lesson_index + 1 WHERE user_id=?", (user_id,))
        conn.commit()


def set_last_sent(user_id: int, ts: int | None = None):
    if ts is None:
        ts = int(time.time())
    with get_conn() as conn:
        c = conn.cursor()
        c.execute("UPDATE users SET last_sent_lesson_at=? WHERE user_id=?", (ts, user_id))
        conn.commit()


def set_last_request(user_id: int, ts: int | None = None):
    if ts is None:
        ts = int(time.time())
    with get_conn() as conn:
        c = conn.cursor()
        c.execute("UPDATE users SET last_request_at=? WHERE user_id=?", (ts, user_id))
        conn.commit()


def reset_manual_if_new_day(user_id: int):
    """
    Если хочешь оставить дневной лимит — сбрасывает счётчик при новом дне (UTC).
    Если лимиты надоели — можешь просто не вызывать её.
    """
    row = get_user(user_id)
    if not row:
        return
    last_req = row[6]  # last_request_at
    now = time.gmtime()
    today_key = f"{now.tm_year}{now.tm_yday}"
    last_key = None
    if last_req:
        t = time.gmtime(last_req)
        last_key = f"{t.tm_year}{t.tm_yday}"
    if last_key != today_key:
        with get_conn() as conn:
            c = conn.cursor()
            c.execute("UPDATE users SET manual_lessons_today=0 WHERE user_id=?", (user_id,))
            conn.commit()


def increment_manual(user_id: int):
    with get_conn() as conn:
        c = conn.cursor()
        c.execute(
            "UPDATE users SET manual_lessons_today = manual_lessons_today + 1 WHERE user_id=?",
            (user_id,)
        )
        conn.commit()


def can_take_manual(user_id: int, max_manual: int) -> bool:
    row = get_user(user_id)
    if not row:
        return False
    return row[3] < max_manual


def mark_blocked(user_id: int):
    with get_conn() as conn:
        c = conn.cursor()
        c.execute("UPDATE users SET status='blocked' WHERE user_id=?", (user_id,))
        conn.commit()


def reactivate_if_blocked(user_id: int):
    row = get_user(user_id)
    if not row:
        return
    if row[7] == 'blocked':
        now = int(time.time())
        with get_conn() as conn:
            c = conn.cursor()
            c.execute(
                "UPDATE users SET status='active', reactivated_at=? WHERE user_id=?",
                (now, user_id)
            )
            conn.commit()


# Оставляем на случай, если где-то ещё вызывается (но антифлуд ты вырубил)
def anti_flood_ok(user_id: int, cooldown: int) -> bool:
    return True  # всегда разрешаем


def get_progress_text(user_id: int, total_lessons: int) -> str:
    row = get_user(user_id)
    if not row:
        return "Нет данных по прогрессу. Нажми /start."
    (
        _uid, level, lesson_index, manual_today,
        start_date, last_sent, last_req, status, reactivated_at
    ) = row
    percent = 0
    if total_lessons > 0:
        percent = min(100, round(lesson_index / total_lessons * 100, 1))
    lines = [
        "📊 Прогресс",
        f"Уровень: {level}",
        f"Уроков: {lesson_index} / {total_lessons}",
        f"Процент: {percent}%",
        f"Ручных сегодня: {manual_today}",
        f"Статус: {status}",
        f"Дата старта: {start_date}",
    ]
    if reactivated_at:
        lines.append("Повторно активирован: да")
    return "\n".join(lines)
