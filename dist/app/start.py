from aiogram import Router,F
from aiogram.filters import CommandStart
from aiogram.types import Message,CallbackQuery
from libs.menu import mStart
from libs.words import wStart
router = Router()

@router.message(CommandStart())
async def start(message:Message):
    await message.answer(wStart.a1.format(i = message.from_user.full_name), reply_markup=mStart.a1)

@router.callback_query(F.data.startswith("start_"))
async def start_callbacks(callback:CallbackQuery):
    action = callback.data.split("_")[1]
    if action == '+':
        return await callback.message.answer("+")
    elif action == '-':
        return await callback.message.answer("-")