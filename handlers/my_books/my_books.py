from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from utils.db_api.schemas.booking import Booking
from keyboards.paginator.booking_paginator import create_booking_paginator_keyboard


async def my_books(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    bookings = await Booking.query.where(Booking.status == "waiting").where(
        Booking.user_id == data['user_id']).gino.all()

    if bookings:
        message = await callback.message.edit_text(text="Ваши брони:",
                                                   reply_markup=await create_booking_paginator_keyboard(state))
        await state.update_data(last_message=message)
    else:
        await callback.message.edit_text(text="Активных броней не найдено",
                                         reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
                                             InlineKeyboardButton(text='В главное меню',
                                                                  callback_data="back_to_main")]]))
