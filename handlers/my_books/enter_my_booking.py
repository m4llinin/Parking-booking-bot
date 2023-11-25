from aiogram.types import CallbackQuery


async def enter_my_booking(callback: CallbackQuery):
    booking_id = callback.data.split('_')[1]
