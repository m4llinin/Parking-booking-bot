#Требует доработки

from aiogram.types import CallbackQuery

async def inline_my_books(callback:CallbackQuery):
    booking = ""
    for i in callback.data:
        if i.isdigit():
            booking+=i
    booking=int(booking)

