import os

from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext


async def activate_booking(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await data['last_message'].delete()
    message = await callback.message.answer(text="Тут должен быть QR-code, но мы его не успели сделать",
                                            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                                                [InlineKeyboardButton(text='Назад',
                                                                      callback_data='back_to_main')]]))
