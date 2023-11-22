from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from lexicon.lexicon_ru import lexicon
from keyboards.main_menu import main_menu


async def start(message: Message, state: FSMContext):
    await state.update_data(parking_page=1, booking_page=1)
    await message.answer(text=lexicon['start'], reply_markup=await main_menu())
