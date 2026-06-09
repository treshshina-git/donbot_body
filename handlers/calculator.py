from aiogram import Router

from aiogram.types import Message
from aiogram.filters import Command

from aiogram.fsm.context import FSMContext

from states.donate_states import DonateWizard

router = Router()


@router.message(Command("calc"))
async def calc_start(
    message: Message,
    state: FSMContext
):

    await message.answer(
        "Сколько чашек кофе вы хотите подарить автору?"
    )

    await state.set_state(
        DonateWizard.coffee_amount
    )


@router.message(
    DonateWizard.coffee_amount
)
async def calc_finish(
    message: Message,
    state: FSMContext
):

    try:

        cups = int(message.text)

        amount = cups * 3

        await message.answer(
            f"""
☕ {'☕' * min(cups, 10)}

Примерная поддержка:

{amount} €

Спасибо ❤️
"""
        )

    except ValueError:

        await message.answer(
            "Введите число."
        )

        return

    await state.clear()