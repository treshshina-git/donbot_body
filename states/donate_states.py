from aiogram.fsm.state import State
from aiogram.fsm.state import StatesGroup


class DonateWizard(StatesGroup):
    donation_type = State()
    telegram_usage = State()
    coffee_amount = State()