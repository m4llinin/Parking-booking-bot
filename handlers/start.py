from aiogram.types import Message
from lexicon.lexicon_ru import lexicon
from keyboards.main_menu import main_menu


async def start(message: Message):
    await message.answer(text=lexicon['start'], reply_markup=main_menu())
