from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from lexicon.lexicon_ru import lexicon
from states.make_booking_state import MakeBooking


async def start_booking(callback: CallbackQuery, state: FSMContext):
    await state.set_state(MakeBooking.wait_location)
    await callback.message.edit_text(text=lexicon['start_booking'])
