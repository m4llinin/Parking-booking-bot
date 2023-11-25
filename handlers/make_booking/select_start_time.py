from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states.make_booking_state import MakeBooking
from aiogram_calendar.simple_calendar import SimpleCalendar


async def select_start_time(callback: CallbackQuery, state: FSMContext):
    selected_time = callback.data.split('_')[1]
    await state.update_data(start_time=selected_time)
    await state.set_state(MakeBooking.END_DATE)

    calendar = SimpleCalendar()
    await callback.message.edit_text(f'Вы выбрали время начала брони: {selected_time}', reply_markup=await calendar.start_calendar())
