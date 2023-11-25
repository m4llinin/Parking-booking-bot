from keyboards.paginator.booking_paginator import count, data
from aiogram.types import CallbackQuery

async def back_my_books(callback: CallbackQuery):
    if(data['booking_page']==1):
        data['booking_page']=count
    else:
        data['booking_page']-=1