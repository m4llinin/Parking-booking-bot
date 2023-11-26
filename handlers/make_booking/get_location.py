import locale

from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram_calendar import CalendarLabels
from aiogram_calendar.simple_calendar import SimpleCalendar

from lexicon.lexicon_ru import lexicon
from states.make_booking_state import MakeBooking


async def get_location(message: Message, state: FSMContext):
    await state.update_data(lat=message.location.latitude)
    await state.update_data(lon=message.location.longitude)

    calendar = SimpleCalendar(CalendarLabels(
                days_of_week=["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"],
                months=["Янв", "Фев", "Март", "Апр", "Май", "Июнь", "Июль", "Авг", "Сен", "Окт", "Ноя", "Дек"],
                cancel_caption='Назад',
                today_caption='Сегодня'
            ))
    await state.set_state(MakeBooking.START_DATE)
    await message.answer(text=lexicon['get_location'], reply_markup=await calendar.start_calendar())
