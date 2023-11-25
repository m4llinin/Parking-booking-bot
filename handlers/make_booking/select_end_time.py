from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from utils.find_nearest_parking import find_nearest_parking
from lexicon.lexicon_ru import lexicon
from keyboards.paginator.parking_paginator import create_parking_paginator_keyboard
import utils.dp_api.db_commands as db


async def select_end_time(callback: CallbackQuery, state: FSMContext):
    selected_time = callback.data.split('_')[1]
    await state.update_data(end_time=selected_time)
    await state.set_state(None)

    data = await state.get_data()
    parking_list = await find_nearest_parking(data['lat'], data['lon'], state)
    await state.update_data(parking_list=parking_list)
    await callback.message.edit_text(f'Вы выбрали время окончания брони: {selected_time}')

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
