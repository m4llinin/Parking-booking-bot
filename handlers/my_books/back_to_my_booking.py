from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.paginator.booking_paginator import create_booking_paginator_keyboard


async def back_to_my_booking(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    try:
        await data['last_location'].delete()
    except KeyError:
        pass

    last_message = data['last_message']
    await last_message.delete()

    await callback.message.answer(text="Вы вернулись в список броней",
                                  reply_markup=await create_booking_paginator_keyboard(state))
