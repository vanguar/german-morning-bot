import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
TIMEZONE = os.getenv("TIMEZONE", "UTC")
AUTOSEND_HOUR = int(os.getenv("AUTOSEND_HOUR", 6))
MAX_MANUAL_PER_DAY = int(os.getenv("MAX_MANUAL_PER_DAY", 2))
NEW_LESSON_COOLDOWN = int(os.getenv("NEW_LESSON_COOLDOWN", 30))
DEFAULT_LEVEL = os.getenv("DEFAULT_LEVEL", "A1")
LESSONS_FILE = os.getenv("LESSONS_FILE", "lessons.json")
LOG_FILE = os.getenv("LOG_FILE", "bot.log")

# ADMIN_IDS = set целых чисел
_admin_raw = os.getenv("ADMIN_IDS", "").strip()
ADMIN_IDS = set()
if _admin_raw:
    for part in _admin_raw.split(","):
        p = part.strip()
        if p.isdigit():
            ADMIN_IDS.add(int(p))
