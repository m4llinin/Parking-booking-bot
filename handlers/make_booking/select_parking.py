from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from keyboards.paginator.parking_places_paginator import create_parking_place_paginator
import utils.dp_api.db_commands as db


async def select_parking(callback: CallbackQuery, state: FSMContext):
    parking_id = callback.data.split("_")[-1]
    await state.update_data(parking=int(parking_id))
    await state.update_data(parking_place_page=1)

    parking = await db.select_parking(int(parking_id))
    await state.update_data(parking_places=parking.places)

    keyboard = await create_parking_place_paginator(state)
    data = await state.get_data()
    await data['last_message'].delete()
    await callback.message.edit_text(text="Выберете парковочное место", reply_markup=keyboard)
