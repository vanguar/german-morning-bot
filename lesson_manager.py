import json
import html
from typing import Dict, List, Any
from config import LESSONS_FILE


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def format_lesson(obj: dict, index: int, total: int) -> str:
    title = esc(obj.get("title", f"Урок {index + 1}"))
    words = obj.get("words", []) or []
    phrases = obj.get("phrases", []) or []
    review = obj.get("review", []) or []
    gram = obj.get("gram", "") or ""
    task = obj.get("task", "") or ""

    parts: List[str] = [f"<b>📘 {title}</b> ({index + 1}/{total})"]

    if words:
        w_block = "\n".join(f"• {esc(de)} — {esc(ru)}" for de, ru in words)
        parts.append("<b>🔤 Слова:</b>\n" + w_block)

    if phrases:
        p_block = "\n".join(f"• {esc(de)} — {esc(ru)}" for de, ru in phrases)
        parts.append("<b>💬 Фразы:</b>\n" + p_block)

    if review:
        r_block = "\n".join(f"• {esc(de)} — {esc(ru)}" for de, ru in review)
        parts.append("<b>♻️ Повтор:</b>\n" + r_block)

    if gram.strip():
        parts.append("<b>⚙️ Грамматика:</b>\n" + esc(gram))

    if task.strip():
        parts.append("<b>📝 Задание:</b>\n" + esc(task))

    return "\n\n".join(parts)


class LessonManager:
    def __init__(self, path: str = LESSONS_FILE):
        self.path = path
        self.data: Dict[str, List[dict]] = {}
        self._load()

    def _load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

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
        if index >= total:
            return self.end_message(level)
        obj = self.get_lesson_obj(level, index)
        if not obj:
            return "❗ Урок не найден."
        return format_lesson(obj, index, total)

    def end_message(self, level: str) -> str:
        other = "A2" if level == "A1" else "A1"
        return (
            f"🏆 <b>Все уроки уровня {level} пройдены!</b>\n"
            f"🔁 Используй «Повторить все» для закрепления.\n"
            f"➡️ Перейти на <b>{other}</b>: отправь <code>{other}</code>.\n"
            "✨ Новые блоки появятся позже."
        )

    def repeat_all(self, level: str, up_to: int) -> List[str]:
        arr = self.data.get(level, [])
        if up_to <= 0:
            return ["Пока нет уроков для повторения. Сначала возьми новый урок 📘."]
        if up_to > len(arr):
            up_to = len(arr)

        total = len(arr)
        out: List[str] = []
        buffer: List[str] = []
        acc = 0

        for i in range(up_to):
            t = format_lesson(arr[i], i, total)
            if acc + len(t) + 2 > 3800 and buffer:
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
