import asyncio
import logging
import time
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramForbiddenError, TelegramRetryAfter, TelegramNetworkError, TelegramAPIError
from config import BOT_TOKEN
from models import get_active_users, get_user, increment_lesson, set_last_sent, mark_blocked
from lesson_manager import LessonManager

logger = logging.getLogger(__name__)
lesson_mgr = LessonManager()

async def send_one(bot: Bot, user_id: int):
    row = get_user(user_id)
    if not row:
        return
    _, level, lesson_index, *_ = row
    total = lesson_mgr.total(level)
    if lesson_index >= total:
        # можно время от времени напоминать
        return
    text = lesson_mgr.current_or_end(level, lesson_index)
    try:
        await bot.send_message(user_id, "🌅 Утренний урок\n\n" + text)
        increment_lesson(user_id)
        set_last_sent(user_id, int(time.time()))
    except TelegramForbiddenError:
        mark_blocked(user_id)
    except TelegramRetryAfter as e:
        await asyncio.sleep(e.retry_after + 1)
        try:
            await bot.send_message(user_id, "🌅 Утренний урок\n\n" + text)
            increment_lesson(user_id)
            set_last_sent(user_id, int(time.time()))
        except TelegramForbiddenError:
            mark_blocked(user_id)
        except Exception as ex:
            logger.error(f"Retry failed user {user_id}: {ex}")
    except (TelegramNetworkError, TelegramAPIError) as e:
        logger.error(f"Network/API error user {user_id}: {e}")

async def broadcast():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN не задан")
    bot = Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    user_ids = get_active_users()
    if not user_ids:
        return
    tasks = [send_one(bot, uid) for uid in user_ids]
    await asyncio.gather(*tasks)
    await bot.session.close()

if __name__ == "__main__":
    from logging_conf import setup_logging
    setup_logging()
    asyncio.run(broadcast())
