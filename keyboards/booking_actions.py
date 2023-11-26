from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def booking_actions_kb():
    button_1 = InlineKeyboardButton(
        text='💵Оплатить',
        callback_data='booking-pay'
    )
    button_2 = InlineKeyboardButton(
        text='🗺️Как добраться?',
        callback_data='help_route'
    )
    button_3 = InlineKeyboardButton(
        text='❌Отменить бронь',
        callback_data='cancel_booking'
    )
    button_4 = InlineKeyboardButton(
        text='Назад',
        callback_data='my_booking'
    )
    inline_kb = [[button_1], [button_2], [button_3], [button_4]]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb)
