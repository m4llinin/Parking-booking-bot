from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext

from utils.db_api.schemas.booking import Booking


async def create_booking_paginator_keyboard(state: FSMContext):
    data = await state.get_data()
    bookings = await Booking.query.where(Booking.status == "waiting").where(
        Booking.user_id == data['user_id']).gino.all()
    await state.update_data(bookings_num=len(bookings))

    page = (data['booking_page'] - 1) * 3

    kb = []

    for i in range(page, page + 3):
        try:
            booking = bookings[i]
            button = InlineKeyboardButton(
                text="Парковка: {} Автомобиль: {}".format(booking.id_parking, booking.vehicle_number),
                callback_data=f"booking_{booking.id}"
            )
            kb.append([button])
        except IndexError:
            break

    count = len(bookings) // 3 + (len(bookings) % 3 != 0)

    kb.append([
        InlineKeyboardButton(text="⬅", callback_data="back_booking_page"),
        InlineKeyboardButton(text="{}/{}".format(data['booking_page'], count), callback_data='just_page'),
        InlineKeyboardButton(text="➡", callback_data="next_booking_page")
    ])
    kb.append([InlineKeyboardButton(
            text="В главное меню", callback_data="back_to_main"
        )])
    return InlineKeyboardMarkup(inline_keyboard=kb)
