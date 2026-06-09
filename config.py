import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

PATREON_LINK = os.getenv("PATREON_LINK")
PAYPAL_LINK = os.getenv("PAYPAL_LINK")
STARS_LINK = os.getenv("STARS_LINK")