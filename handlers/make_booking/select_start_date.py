from aiogram_calendar import SimpleCalendar, SimpleCalendarCallback
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from states.make_booking_state import MakeBooking
from keyboards.paginator.selection_time import selection_time


async def select_start_date(callback: CallbackQuery, callback_data: SimpleCalendarCallback, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback, callback_data)
    await state.update_data(time_page=1)
    if selected:
        await state.update_data(start_date=date)
        await state.set_state(MakeBooking.START_TIME)
        await callback.message.edit_text(f'Вы выбрали дату начала брони: {date.strftime("%d.%m.%Y")}\nТеперь выберете время',
                                         reply_markup=await selection_time(state))
