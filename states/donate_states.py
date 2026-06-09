from aiogram.fsm.state import State, StatesGroup

class DonateWizard(StatesGroup):
donation_type = State()
telegram_usage = State()
