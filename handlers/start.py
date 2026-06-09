from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.donate_kb import start_kb

router = Router()


@router.message(CommandStart())
async def start(message: Message):

    await message.answer(
        """
🧭 Привет!

Я Donate Wizard.

Помогу выбрать лучший способ
поддержать автора за несколько секунд.

Команды:

/donate
/calc
/support
/why
""",
        reply_markup=start_kb
    )