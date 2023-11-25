from keyboards.paginator.booking_paginator import count, data
from aiogram.types import CallbackQuery

async def next_my_books(callback: CallbackQuery):
    if(data['booking_page']==count):
        data['booking_page']=1
    else:
        data['booking_page']+=1
