from aiogram.utils.keyboard import InlineKeyboardBuilder

FILES_CACHE = {}


def consoles_kb():
    kb = InlineKeyboardBuilder()

    for c in ("NES", "SNES", "SEGA"):
        kb.button(
            text=c,
            callback_data=f"console:{c}"
        )

    kb.adjust(1)

    return kb.as_markup()


def files_kb(user_id, console, files):
    kb = InlineKeyboardBuilder()

    FILES_CACHE[user_id] = {}

    for i, file in enumerate(files):
        FILES_CACHE[user_id][str(i)] = (console, file)

        kb.button(
            text=file[:50],
            callback_data=f"rom:{i}"
        )

    kb.button(
        text="◀️ НАЗАД",
        callback_data="back"
    )

    kb.adjust(1)

    return kb.as_markup()
