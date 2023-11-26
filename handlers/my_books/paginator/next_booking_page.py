from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.paginator.booking_paginator import create_booking_paginator_keyboard


async def next_booking_page(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    if data['booking_page'] == data['bookings_num'] // 3 + (data['bookings_num'] % 3 != 0):
        await callback.answer(text="Вы на последней странице")
        return
    await state.update_data(booking_page=data['booking_page'] + 1)

    await callback.message.delete()
    await callback.message.answer(text="Ваши брони:", reply_markup=await create_booking_paginator_keyboard(state))
