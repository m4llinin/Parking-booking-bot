from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext


async def booking_actions_kb(state: FSMContext):
    data = await state.get_data()
    if data['status'] != 'waiting':
        button_1 = InlineKeyboardButton(
            text='🆔Показать QR-код',
            callback_data='activate_booking'
        )
    else:
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
