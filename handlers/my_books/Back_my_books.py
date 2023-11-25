from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext

from keyboards.paginator.CallbackDataClassPaginator import Booking


async def create_booking_paginator_keyboard(bookings: list, state: FSMContext):
    data = await state.get_data()
    count = len(bookings) // 3 + (len(bookings) % 3 != 0)
    if (data['booking_page'] == 1):
        data['booking_page'] = count
    else:
        data['booking_page'] -= 1
    page = (data['booking_page'] - 1) * 3

    kb = []

    for i in range(page, page + 3):
        if(i>len(bookings)-1):
            break
        booking = bookings[i]
        button = InlineKeyboardButton(
            text="Парковка: {} Автомобиль: {}".format(booking.id_parking, booking.vehicle_number),
            callback_data=f"booking_{booking.id}"
        )
        kb.append([button])

    kb += [
        InlineKeyboardButton(text="⬅", callback_data="back_booking_page"),
        InlineKeyboardButton(text="{}/{}".format(data['booking_page'], count), callback_data='just_page'),
        InlineKeyboardButton(text="➡", callback_data="next_booking_page")
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)