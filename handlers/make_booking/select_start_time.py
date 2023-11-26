from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram_calendar import CalendarLabels

from states.make_booking_state import MakeBooking
from aiogram_calendar.simple_calendar import SimpleCalendar


async def select_start_time(callback: CallbackQuery, state: FSMContext):
    selected_time = callback.data.split('_')[1]
    await state.update_data(start_time=selected_time)
    await state.set_state(MakeBooking.END_DATE)

    calendar = SimpleCalendar(CalendarLabels(
                days_of_week=["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
                months=["Янв", "Фев", "Март", "Апр", "Май", "Июнь", "Июль", "Авг", "Сен", "Окт", "Ноя", "Дек"],
                cancel_caption='Назад',
                today_caption='Сегодня'
            ))
    await callback.message.edit_text(f'Вы выбрали время начала брони: {selected_time}', reply_markup=await calendar.start_calendar())
