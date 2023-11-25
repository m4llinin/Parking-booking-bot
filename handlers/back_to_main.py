from aiogram.types import CallbackQuery
from keyboards.main_menu import main_menu


async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(text="Вы вернулись в главное меню", reply_markup=await main_menu())
