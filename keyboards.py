from aiogram.utils.keyboard import InlineKeyboardBuilder

def consoles_kb():
    kb = InlineKeyboardBuilder()
    for c in ("NINTENDO", "SUPERNINTENDO", "SEGA"):
        kb.button(text=c, callback_data=f"console:{c}")
    kb.adjust(1)
    return kb.as_markup()

def files_kb(console, files):
    kb = InlineKeyboardBuilder()
    for f in files:
        kb.button(text=f, callback_data=f"rom:{console}:{f}")
    kb.button(text="⬅️ Back", callback_data="back")
    kb.adjust(1)
    return kb.as_markup()
