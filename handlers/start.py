from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.donate_kb import start_kb

router = Router()

@router.message(CommandStart())
async def start(message: Message):

```
await message.answer(
    """
```

🧭 Donate Wizard

Помогу подобрать самый удобный
способ поддержки автора.

Нажмите кнопку ниже.
""",
reply_markup=start_kb
)
