from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.donate_kb import start_kb

router = Router()
@router.message()
async def test(message: Message):
    print("Получено:", message.text)

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🧭 Donate Wizard\n\nНажмите кнопку ниже.",
        reply_markup=start_kb
    )
