from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from states.donate_states import DonateWizard

from keyboards.donate_kb import (
donation_type_kb,
telegram_kb,
restart_kb
)

from config import (
PATREON_LINK,
PAYPAL_LINK,
STARS_LINK
)

router = Router()

@router.message(Command("donate"))
async def donate(
message: Message,
state: FSMContext
):
await message.answer(
"🧭 Какой вариант вам ближе?",
reply_markup=donation_type_kb
)

```
await state.set_state(
    DonateWizard.donation_type
)
```

@router.callback_query(F.data == "start_donate")
async def start_donate(
callback: CallbackQuery,
state: FSMContext
):
await callback.message.edit_text(
"🧭 Какой вариант вам ближе?",
reply_markup=donation_type_kb
)

```
await state.set_state(
    DonateWizard.donation_type
)

await callback.answer()
```

@router.callback_query(
DonateWizard.donation_type,
F.data == "regular"
)
async def regular(
callback: CallbackQuery,
state: FSMContext
):
await callback.message.edit_text(
f"""
❤️ Patreon

Подходит для регулярной поддержки.

🔗 {PATREON_LINK}
""",
reply_markup=restart_kb
)

```
await state.clear()
await callback.answer()
```

@router.callback_query(
DonateWizard.donation_type,
F.data == "fast"
)
async def fast(
callback: CallbackQuery,
state: FSMContext
):
await callback.message.edit_text(
"""
📱 Пользуетесь Telegram каждый день?

Это поможет подобрать
самый быстрый вариант.
""",
reply_markup=telegram_kb
)

```
await state.set_state(
    DonateWizard.telegram_usage
)

await callback.answer()
```

@router.callback_query(
DonateWizard.donation_type,
F.data == "thanks"
)
async def thanks(
callback: CallbackQuery,
state: FSMContext
):
await callback.message.edit_text(
f"""
💳 PayPal

Отличный вариант для разового доната.

🔗 {PAYPAL_LINK}
""",
reply_markup=restart_kb
)

```
await state.clear()
await callback.answer()
```

@router.callback_query(
DonateWizard.telegram_usage,
F.data == "tg_yes"
)
async def tg_yes(
callback: CallbackQuery,
state: FSMContext
):
await callback.message.edit_text(
f"""
⭐ Telegram Stars

Самый быстрый способ поддержки.

🔗 {STARS_LINK}
""",
reply_markup=restart_kb
)

```
await state.clear()
await callback.answer()
```

@router.callback_query(
DonateWizard.telegram_usage,
F.data == "tg_no"
)
async def tg_no(
callback: CallbackQuery,
state: FSMContext
):
await callback.message.edit_text(
f"""
💳 PayPal

Для вас это будет наиболее удобный вариант.

🔗 {PAYPAL_LINK}
""",
reply_markup=restart_kb
)

```
await state.clear()
await callback.answer()
```
