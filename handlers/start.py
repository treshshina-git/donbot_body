from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def any_message(message: Message):
    print("Получено:", message.text)
    await message.answer("Я получил сообщение")
