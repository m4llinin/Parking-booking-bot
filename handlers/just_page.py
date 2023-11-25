from aiogram.types import CallbackQuery


async def just_page(callback: CallbackQuery):
    await callback.answer(text="Это просто страница😜")
