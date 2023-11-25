from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext


async def create_booking_paginator_keyboard(bookings: list, state: FSMContext):
    data = await state.get_data()
    page = (data['booking_page'] - 1) * 3

    kb = []

    for i in range(page, page + 3):
        booking = bookings[i]
        button = InlineKeyboardButton(
            text="Парковка: {} Автомобиль: {}".format(booking.id_parking, booking.vehicle_number),
            callback_data=f"booking_{booking.id}"
        )
        kb.append([button])

    count = len(bookings) // 3 + (len(bookings) % 3 != 0)

    kb += [
        InlineKeyboardButton(text="⬅", callback_data="back_booking_page"),
        InlineKeyboardButton(text="{}/{}".format(data['booking_page'], count), callback_data='just_page'),
        InlineKeyboardButton(text="➡", callback_data="next_booking_page")
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)
