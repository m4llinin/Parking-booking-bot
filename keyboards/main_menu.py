from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def main_menu():
    button_1 = InlineKeyboardButton(
        text='🚀Забронировать',
        callback_data='to_book'
    )
    button_2 = InlineKeyboardButton(
        text='📌Мои брони',
        callback_data='my_booking'
    )
    button_3 = InlineKeyboardButton(
        text='⚙Тех.поддержка',
        callback_data='support'
    )
    inline_kb = [[button_1], [button_2], [button_3]]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb)
