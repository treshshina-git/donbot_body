import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router

dp = Dispatcher()
dp.include_router(router)

async def main():
    bot = Bot(BOT_TOKEN)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
