from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery, URLInputFile
from keyboards import (
    consoles_kb,
    files_kb,
    FILES_CACHE
)
from aiohttp import ClientResponseError
from github_api import get_files, OWNER, REPO

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("🎮 Выберите приставку:", reply_markup=consoles_kb())

@router.callback_query(F.data == "back")
async def back(callback: CallbackQuery):
    await callback.message.edit_text("🎮 Выберите приставку:", reply_markup=consoles_kb())
    await callback.answer()

@router.callback_query(F.data.startswith("console:"))
async def choose_console(callback: CallbackQuery):
    console = callback.data.split(":", 1)[1]
    files = await get_files(console)

    await callback.message.edit_text(
        f"🕹️ Игры для {console}:",
        reply_markup=files_kb(
            callback.from_user.id,
            console,
            files
        )
    )
    await callback.answer()

@router.callback_query(F.data.startswith("rom:"))
async def send_rom(callback: CallbackQuery):

    file_id = callback.data.split(":")[1]

    console, filename = FILES_CACHE[
        callback.from_user.id
    ][file_id]

    raw_url = (
        f"https://raw.githubusercontent.com/"
        f"{OWNER}/{REPO}/main/"
        f"ROMs%20for%20Play/{console}/{filename}"
    )
    try:
        await callback.message.answer_document(
            URLInputFile(raw_url),
            caption=filename
        )
    except (ClientResponseError, ClientError, TelegramBadRequest):
        await callback.message.answer("❌ ROM недоступен или не найден")

    await callback.answer()
