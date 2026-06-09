from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

restart_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔄 Начать заново",
                callback_data="start_donate"
            )
        ]
    ]
)

start_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🚀 Подобрать способ",
                callback_data="start_donate"
            )
        ]
    ]
)

donation_type_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="❤️ Регулярно",
                callback_data="regular"
            )
        ],
        [
            InlineKeyboardButton(
                text="⚡ Быстро",
                callback_data="fast"
            )
        ],
        [
            InlineKeyboardButton(
                text="🎁 Просто поблагодарить",
                callback_data="thanks"
            )
        ]
    ]
)

telegram_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Да",
                callback_data="tg_yes"
            )
        ],
        [
            InlineKeyboardButton(
                text="Нет",
                callback_data="tg_no"
            )
        ]
    ]
)
