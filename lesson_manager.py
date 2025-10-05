# lesson_manager.py
import json
import html
import logging
from typing import Dict, List, Any
from config import LESSONS_FILE

# Порядок уровней для вычисления «следующего»
LEVELS_ORDER = ["A1", "A2", "B1", "B2"]



def esc(text: str) -> str:
    return html.escape(text, quote=False)

# Полностью обновлённая функция форматирования урока
def format_lesson(obj: dict, index: int, total: int) -> str:
    title = esc(obj.get("title", f"Урок {index + 1}"))
    words = obj.get("words", []) or []
    phrases = obj.get("phrases", []) or []
    review = obj.get("review", []) or []
    gram = obj.get("gram", {}) or {} # Теперь это объект
    task = obj.get("task", "") or ""

    parts: List[str] = [f"<b>📘 {title}</b> ({index + 1}/{total})"]

    if words:
        w_block = "\n".join(f"• <code>{esc(de)}</code> — {esc(ru)}" for de, ru in words)
        parts.append("<b>🔤 Новые слова:</b>\n" + w_block)

    if phrases:
        p_block = "\n".join(f"• <i>{esc(de)}</i>\n  — {esc(ru)}" for de, ru in phrases)
        parts.append("<b>💬 Фразы для запоминания:</b>\n" + p_block)

    # Новый блок для обработки грамматики
    if gram and gram.get("rule"):
        gram_parts = []
        # Основное правило
        gram_parts.append(f"<b>⚙️ Грамматика:</b> {esc(gram['rule'])}")

        # Таблица (если есть)
        if gram.get("table"):
            table_str = "\n".join(" | ".join(f"<code>{esc(cell)}</code>" for cell in row) for row in gram["table"])
            gram_parts.append(f"<b>📋 Таблица:</b>\n{table_str}")

        # Примеры (если есть)
        if gram.get("examples"):
            examples_str = "\n".join(f"• <i>{esc(de)}</i> — {esc(ru)}" for de, ru in gram["examples"])
            gram_parts.append(f"<b>✨ Примеры:</b>\n{examples_str}")
        
        parts.append("\n\n".join(gram_parts))

    if review:
        r_block = "\n".join(f"• <code>{esc(de)}</code> — {esc(ru)}" for de, ru in review)
        parts.append("<b>♻️ Повторение:</b>\n" + r_block)

    if task.strip():
        parts.append("<b>📝 Задание:</b>\n" + esc(task))

    return "\n\n".join(parts)


class LessonManager:
    def __init__(self, path: str = LESSONS_FILE):
        self.path = path
        self.data: Dict[str, List[dict]] = {}
        self._load()
        # 🔧 Добавлено: подхват внешних модулей с уроками (B1/B2)
        self._merge_external()

    # после self._load() в __init__ или в конце _load()
    def _merge_external(self):
        import importlib, logging
        for mod_name in ("lessons_b1", "lessons_b2"):
            try:
                mod = importlib.import_module(mod_name)
                level = getattr(mod, "LEVEL", mod_name.split("_")[-1].upper())
                lessons = getattr(mod, "LESSONS", [])
                if lessons:
                    self.data[level] = lessons
                    logging.info("Loaded external lessons for %s: %d", level, len(lessons))
            except Exception as e:
                logging.info("No external lessons module %s: %s", mod_name, e)    

    def _load(self):
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"Could not load or parse lessons file: {e}")
            self.data = {}

    def reload(self):
        self._load()

    def total(self, level: str) -> int:
        return len(self.data.get(level, []))

    def get_lesson_obj(self, level: str, index: int) -> Any:
        arr = self.data.get(level, [])
        if 0 <= index < len(arr):
            return arr[index]
        return None

    def current_or_end(self, level: str, index: int) -> str:
        total = self.total(level)
        if total == 0:
            return f"❗ Уроки для уровня {level} не найдены или файл {self.path} пуст."
        if index >= total:
            return self.end_message(level)
        obj = self.get_lesson_obj(level, index)
        if not obj:
            return "❗ Урок не найден."
        return format_lesson(obj, index, total)

    def end_message(self, level: str) -> str:
        # найдём «следующий» уровень по цепочке, который реально есть в данных
        next_level = None
        try:
            idx = LEVELS_ORDER.index(level)
        except ValueError:
            idx = -1
        if idx >= 0:
            for lv in LEVELS_ORDER[idx + 1:]:
                if self.total(lv) > 0:
                    next_level = lv
                    break

        lines = [
            f"🏆 <b>Все уроки уровня {level} пройдены!</b>",
            "🔁 Используйте «Повторить все» для закрепления.",
        ]
        if next_level:
            lines.append(f"➡️ Попробуйте перейти на <b>{next_level}</b>, отправив /start и выбрав уровень.")
        else:
            lines.append("✨ Новые блоки уроков появятся позже.")
        return "\n".join(lines)


    def repeat_all(self, level: str, up_to: int) -> List[str]:
        arr = self.data.get(level, [])
        if up_to <= 0:
            return ["Пока нет уроков для повторения. Сначала возьмите новый урок 📘."]
        if up_to > len(arr):
            up_to = len(arr)

        total = len(arr)
        out: List[str] = []
        buffer: List[str] = []
        acc = 0

        for i in range(up_to):
            t = format_lesson(arr[i], i, total)
            # Telegram message length limit is 4096
            if acc + len(t) + 2 > 4000 and buffer:
                out.append("\n\n".join(buffer))
                buffer = [t]
                acc = len(t)
            else:
                buffer.append(t)
                acc += len(t) + 2

        if buffer:
            out.append("\n\n".join(buffer))

        if out:
            out[0] = "<b>🔁 Повторение изученных уроков</b>\n\n" + out[0]

        return out
