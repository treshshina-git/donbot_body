from aiogram import Router
from aiogram import F

from aiogram.types import Message
from aiogram.types import CallbackQuery

from aiogram.filters import Command

from aiogram.fsm.context import FSMContext

from states.donate_states import DonateWizard

from keyboards.donate_kb import (
    donation_type_kb,
    telegram_kb
)

from config import (
    PATREON_LINK,
    PAYPAL_LINK,
    STARS_LINK
)

router = Router()


@router.message(Command("support"))
async def support(message: Message):

    await message.answer(
        f"""
❤️ Patreon
{PATREON_LINK}

💳 PayPal
{PAYPAL_LINK}

⭐ Stars
{STARS_LINK}
"""
    )


@router.message(Command("why"))
async def why(message: Message):

    await message.answer(
        """
🎉 Каждый донат помогает:

• оплачивать Railway
• оплачивать API
• выпускать новый контент
• развивать проект
"""
    )


@router.message(Command("donate"))
async def donate(
    message: Message,
    state: FSMContext
):

    await message.answer(
        "Какой вариант вам ближе?",
        reply_markup=donation_type_kb
    )

    await state.set_state(
        DonateWizard.donation_type
    )


@router.callback_query(
    F.data == "start_donate"
)
async def start_button(
    callback: CallbackQuery,
    state: FSMContext
):

    await callback.message.answer(
        "Какой вариант вам ближе?",
        reply_markup=donation_type_kb
    )

    await state.set_state(
        DonateWizard.donation_type
    )


@router.callback_query(
    DonateWizard.donation_type,
    F.data == "regular"
)
async def regular(
    callback: CallbackQuery,
    state: FSMContext
):

    await callback.message.answer(
        f"""
❤️ Patreon

Лучший вариант для регулярной поддержки.

{PATREON_LINK}
"""
    )

    await state.clear()


@router.callback_query(
    DonateWizard.donation_type,
    F.data == "fast"
)
async def fast(
    callback: CallbackQuery,
    state: FSMContext
):

    await callback.message.answer(
        "Пользуетесь Telegram ежедневно?",
        reply_markup=telegram_kb
    )

    await state.set_state(
        DonateWizard.telegram_usage
    )


@router.callback_query(
    DonateWizard.donation_type,
    F.data == "thanks"
)
async def thanks(
    callback: CallbackQuery,
    state: FSMContext
):

    await callback.message.answer(
        f"""
💳 Для разовой благодарности
отлично подойдёт PayPal.

{PAYPAL_LINK}
"""
    )

    await state.clear()


@router.callback_query(
    DonateWizard.telegram_usage,
    F.data == "tg_yes"
)
async def tg_yes(
    callback: CallbackQuery,
    state: FSMContext
):

    await callback.message.answer(
        f"""
⭐ Telegram Stars

Самый быстрый способ поддержки.

{STARS_LINK}
"""
    )

    await state.clear()


@router.callback_query(
    DonateWizard.telegram_usage,
    F.data == "tg_no"
)
async def tg_no(
    callback: CallbackQuery,
    state: FSMContext
):

    await callback.message.answer(
        f"""
💳 PayPal

Удобный вариант для разового доната.

{PAYPAL_LINK}
"""
    )

    await state.clear()