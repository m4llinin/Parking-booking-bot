from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from states.make_booking_state import MakeBooking


async def enter_vehicle_number(callback: CallbackQuery, state: FSMContext):
    await state.set_state(MakeBooking.VEHICLE_NUMBER)
    await state.update_data(place=callback.data.split("_")[1])
    await callback.message.answer(text="Напишите номер автомобиля, на котором вы приедете (в формате А000АА178)")