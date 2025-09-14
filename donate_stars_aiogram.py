# -*- coding: utf-8 -*-
# Простая витрина Telegram Stars (aiogram v3)
import os
from aiogram import F
from aiogram.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    PreCheckoutQuery, Message, LabeledPrice
)
from aiogram import Bot, Dispatcher

PROVIDER_TOKEN = os.getenv("TELEGRAM_STARS_PROVIDER_TOKEN", "")  # можно оставить пустым для цифровых товаров
CURRENCY = "XTR"

# Небольшой набор пресетов, чтобы не хранить состояние для «+/-»
PRESETS = [10, 15, 25, 50, 100, 200]

def build_donate_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✨ Поддержать звёздами", callback_data="donate_menu")]
    ])

def _menu_kb() -> InlineKeyboardMarkup:
    row1 = [InlineKeyboardButton(f"💖 {PRESETS[1]}⭐", callback_data=f"donate_pick:{PRESETS[1]}"),
            InlineKeyboardButton(f"🎁 {PRESETS[2]}⭐", callback_data=f"donate_pick:{PRESETS[2]}"),
            InlineKeyboardButton(f"🏆 {PRESETS[4]}⭐", callback_data=f"donate_pick:{PRESETS[4]}")]
    row2 = [InlineKeyboardButton(f"⭐ {p}", callback_data=f"donate_pick:{p}") for p in (PRESETS[0], PRESETS[3], PRESETS[5])]
    return InlineKeyboardMarkup(inline_keyboard=[row1, row2, [InlineKeyboardButton("⬅️ Закрыть", callback_data="donate_close")]])

async def donate_menu_handler(callback_query, bot: Bot):
    await callback_query.answer()
    await callback_query.message.answer("✨ Выберите сумму в звёздах:", reply_markup=_menu_kb())

async def donate_close_handler(callback_query, bot: Bot):
    await callback_query.answer("Закрыто")
    try:
        await callback_query.message.delete()
    except Exception:
        pass

async def donate_pick_handler(callback_query, bot: Bot):
    await callback_query.answer()
    try:
        stars = int(callback_query.data.split(":")[1])
    except Exception:
        return
    prices = [LabeledPrice(label=f"Поддержка ⭐ {stars}", amount=stars)]
    await bot.send_invoice(
        chat_id=callback_query.from_user.id,
        title=f"⭐ Поддержка ({stars})",
        description="Спасибо за вклад в развитие бота!",
        payload=f"stars:{stars}",
        provider_token=PROVIDER_TOKEN,
        currency=CURRENCY,
        prices=prices,
    )

async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    # обязателен ответ ok=True
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

async def successful_payment_handler(message: Message):
    sp = message.successful_payment
    stars = sp.total_amount  # для XTR «минимальная единица» == звезда
    user_name = message.from_user.first_name or (message.from_user.username and f"@{message.from_user.username}") or "друг"
    await message.answer(f"✨ Спасибо, {user_name}! Получено {stars}⭐ — это очень помогает 🙏")

def register_donate_handlers(dp: Dispatcher):
    dp.callback_query.register(donate_menu_handler, F.data == "donate_menu")
    dp.callback_query.register(donate_close_handler, F.data == "donate_close")
    dp.callback_query.register(donate_pick_handler, F.data.startswith("donate_pick:"))
    dp.pre_checkout_query.register(pre_checkout_handler)
    dp.message.register(successful_payment_handler, F.successful_payment)
