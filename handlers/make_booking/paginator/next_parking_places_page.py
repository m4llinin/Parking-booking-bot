from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.paginator.parking_places_paginator import create_parking_place_paginator


async def next_parking_places_page(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if data['parking_place_page'] == (len(data['parking_places']) // 49 + (len(data['parking_places']) % 49 != 0)):
        await callback.answer(text="Вы на последней странице")
        return
    await state.update_data(parking_place_page=data['parking_place_page'] + 1)

    await callback.message.delete()
    await callback.message.answer(text="Выберете парковочное место",
                                  reply_markup=await create_parking_place_paginator(state))
