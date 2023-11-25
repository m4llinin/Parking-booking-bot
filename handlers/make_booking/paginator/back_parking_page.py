from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from lexicon.lexicon_ru import lexicon
from keyboards.paginator.parking_paginator import create_parking_paginator_keyboard
import utils.dp_api.db_commands as db


async def back_parking_page(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if data['parking_page'] == 1:
        await callback.answer(text="Вы на первой странице")
        return
    page = data['parking_page'] - 1
    await state.update_data(parking_page=page)

    await data['last_message'].delete()
    await callback.message.delete()

    parking_list = data['parking_list']

    if parking_list:
        cur_parking = await db.select_parking(parking_list[data['parking_page'] - 1][0])
        message = await callback.message.answer_location(latitude=cur_parking.latitude, longitude=cur_parking.longitude)
        await state.update_data(last_message=message)
        await callback.message.answer(
            text=lexicon['paginator_parking'].format(cur_parking.id, cur_parking.all_places, cur_parking.free_places),
            reply_markup=await create_parking_paginator_keyboard(cur_parking.id, len(parking_list), state)
        )
    else:
        await callback.message.answer(text="Парковок не найдено")
