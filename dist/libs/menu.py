from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup


class mStart:
    a1 = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="+",callback_data="start_+"),
            InlineKeyboardButton(text="-",callback_data="start_-")
        ]
    ])