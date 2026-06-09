import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from handlers.start import router as start_router
from handlers.donate import router as donate_router
from handlers.calculator import router as calc_router

async def main():

```
bot = Bot(BOT_TOKEN)

await bot.delete_webhook(
    drop_pending_updates=True
)

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(donate_router)
dp.include_router(calc_router)

print("Бот запущен")

await dp.start_polling(bot)
```

if **name** == "**main**":
asyncio.run(main())
