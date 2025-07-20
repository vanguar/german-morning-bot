"""
Хранилище уроков (пока в коде).
Следующий спринт — вынести в JSON/БД.
"""

# Примерные массивы. Можно расширять.
LESSONS = {
    "A1": [
        "Урок A1 #1\nПриветствия:\nHallo — Привет\nGuten Morgen — Доброе утро\nIch heiße ... — Меня зовут ...\n\nФраза дня: Wie geht es dir? — Как у тебя дела?",
        "Урок A1 #2\nЧисла 1–5:\nEins, Zwei, Drei, Vier, Fünf.\nСтруктура предложения: Ich bin ... / Ich komme aus ...",
        "Урок A1 #3\nБазовые глаголы:\nsein (быть), haben (иметь), machen (делать).\nПример: Ich habe einen Bruder — У меня есть брат."
    ],
    "A2": [
        "Урок A2 #1\nПовторение A1 + расширение словаря: arbeiten (работать), lernen (учиться).",
        "Урок A2 #2\nПрошедшее время Perfekt (ввод): Ich habe gespielt.",
        "Урок A2 #3\nМодальные глаголы (dürfen, wollen) — базовое введение."
    ]
}

# Максимальные уроки по уровню (для прогресса).
TOTAL_LESSONS = {lvl: len(lst) for lvl, lst in LESSONS.items()}


def total_for_level(level: str) -> int:
    return TOTAL_LESSONS.get(level, 0)


def get_lesson_text(level: str, index: int) -> str:
    lessons = LESSONS.get(level, [])
    if 0 <= index < len(lessons):
        return lessons[index]
    return ""


def is_last_lesson(level: str, index: int) -> bool:
    lessons = LESSONS.get(level, [])
    return index >= len(lessons)


def build_end_message(level: str) -> str:
    return (f"🔥 Ты прошёл все доступные уроки уровня {level}!\n"
            f"Можешь повторять материал или перейти на другой уровень.")


def get_repeat_all(level: str, up_to_index: int) -> str:
    """
    Вернёт все пройденные уроки (0..up_to_index-1).
    Если ничего не пройдено — информирующее сообщение.
    """
    lessons = LESSONS.get(level, [])
    if up_to_index <= 0:
        return "Пока нет уроков для повторения. Пройди хотя бы один новый."
    slice_part = lessons[:up_to_index]
    if not slice_part:
        return "Пока нет уроков для повторения."
    return "🔁 Повторение всех пройденных уроков:\n\n" + "\n\n---\n\n".join(slice_part)


def get_current_lesson_or_end(level: str, index: int) -> str:
    lessons = LESSONS.get(level, [])
    if index >= len(lessons):
        # вернём последнее + сообщение
        if lessons:
            last = lessons[-1]
            return last + "\n\n" + build_end_message(level)
        return build_end_message(level)
    return lessons[index]
