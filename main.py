import json
import os
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton
)

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()

with open("services.json", "r", encoding="utf-8") as f:
    SERVICES = json.load(f)

user_data = {}

mode_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💸 Разовый донат")],
        [KeyboardButton(text="⭐ Подписка")]
    ],
    resize_keyboard=True
)

country_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇩🇪 Германия")],
        [KeyboardButton(text="🇺🇸 США")],
        [KeyboardButton(text="🌍 Другая")]
    ],
    resize_keyboard=True
)

payment_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💳 Карта")],
        [KeyboardButton(text="🅿️ PayPal")],
        [KeyboardButton(text="⭐ Telegram Stars")]
    ],
    resize_keyboard=True
)

@dp.message(CommandStart())
async def start(message: Message):
    user_data[message.from_user.id] = {}
    await message.answer(
        "Как вы хотите поддержать автора?",
        reply_markup=mode_keyboard
    )

@dp.message(F.text == "💸 Разовый донат")
async def donate(message: Message):
    user_data[message.from_user.id]["mode"] = "donate"
    await message.answer(
        "Из какой вы страны?",
        reply_markup=country_keyboard
    )

@dp.message(F.text == "⭐ Подписка")
async def subscription(message: Message):
    user_data[message.from_user.id]["mode"] = "subscription"
    await message.answer(
        "Из какой вы страны?",
        reply_markup=country_keyboard
    )

@dp.message(F.text.in_(["🇩🇪 Германия", "🇺🇸 США", "🌍 Другая"]))
async def country(message: Message):

    mapping = {
        "🇩🇪 Германия": "Germany",
        "🇺🇸 США": "USA",
        "🌍 Другая": "Other"
    }

    user_data[message.from_user.id]["country"] = mapping[message.text]

    await message.answer(
        "Как вам удобнее платить?",
        reply_markup=payment_keyboard
    )

@dp.message(F.text.in_([
    "💳 Карта",
    "🅿️ PayPal",
    "⭐ Telegram Stars"
]))
async def payment(message: Message):

    payment_map = {
        "💳 Карта": "card",
        "🅿️ PayPal": "paypal",
        "⭐ Telegram Stars": "stars"
    }

    uid = message.from_user.id

    payment_type = payment_map[message.text]
    country = user_data[uid]["country"]
    mode = user_data[uid]["mode"]

    best = None
    best_score = -1

    for service in SERVICES.values():

        score = 0

        if country in service["countries"]:
            score += 5

        if mode == "donate" and service["donate"]:
            score += 5

        if mode == "subscription" and service["subscription"]:
            score += 5

        if payment_type == "card" and service["card"]:
            score += 3
        if payment_type == "paypal" and service["paypal"]:
            score += 3

        if payment_type == "stars" and service["stars"]:
            score += 3

        if score > best_score:
            best_score = score
            best = service

    await message.answer(
        f"🏆 Лучший вариант:\n\n"
        f"{best['name']}\n\n"
        f"Ссылка:\n{best['link']}"
    )

async def main():
    await dp.start_polling(bot)

if best["name"] == "main":
    asyncio.run(main())
