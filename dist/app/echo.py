from aiogram import Router
from aiogram.types import Message
from libs.decorators import TestDecorator
router = Router()

@router.message()
@TestDecorator
async def echo(message:Message):
    return await message.answer(message.text)
