# users_db.py
"""
Заглушка для обратной совместимости.
Ранее функционал был тут, теперь всё перенесено в models.py.
Импорты из старого кода продолжат работать.
"""
from models import (
    init_db,
    register_user,
    get_user as get_user_row,
    get_active_users as get_all_active_user_ids,
    set_level as update_level,
    increment_lesson as increment_lesson_index,
    set_last_sent,
    set_last_request,
    reset_manual_if_new_day as reset_manual_counter_if_new_day,
    increment_manual as increment_manual_lessons,
    can_take_manual as can_take_manual_lesson,
    anti_flood_ok,
    mark_blocked,
    get_progress_text,
)
