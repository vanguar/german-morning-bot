# German Morning Mini Tutor Bot (aiogram 3)

## Что это
Телеграм-бот с утренним авто-уроком + ручными уроками немецкого (A1/A2). Лимиты, анти-флуд, реактивация, JSON-контент, логирование.

## Возможности
- /start — регистрация, реактивация (если был blocked)
- Уровни A1 / A2 (сообщением)
- Авто-урок утром (через cron + `daily_send.py`)
- До 2 новых уроков вручную в день (кнопка 📘)
- Повтор всех пройденных (🔁)
- Прогресс (📈 или /progress)
- Анти-флуд (30 сек)
- Статусы: active / blocked (blocked ставится при запрете отправки)
- JSON-файл `lessons.json` — легко расширять контент
- Логи (rotating) — файл `bot.log`
- Таблица `user_errors` (пока под будущее: тесты / фиксация ошибок)

## Установка
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
# вставь BOT_TOKEN
python bot.py
