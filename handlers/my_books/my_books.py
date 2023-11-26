from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from utils.db_api.schemas.booking import Booking
from keyboards.paginator.booking_paginator import create_booking_paginator_keyboard


async def my_books(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    """bookings = await Booking.query.where(Booking.status == "waiting").where(
        Booking.user_id == data['user_id']).gino.all()

    await state.update_data(bookings=bookings)"""
    message = await callback.message.edit_text(text="Ваши брони:",
                                               reply_markup=await create_booking_paginator_keyboard(state))
    await state.update_data(last_message=message)
