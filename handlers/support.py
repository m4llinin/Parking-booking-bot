from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import lexicon


async def support(callback: CallbackQuery):
    button = InlineKeyboardButton(
        text="В главное меню", callback_data="back_to_main"
    )
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await callback.message.edit_text(lexicon['tech_support'], reply_markup=keyboard)
