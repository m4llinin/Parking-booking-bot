from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext


async def create_parking_paginator_keyboard(parking_id: int, count: int, state: FSMContext):
    data = await state.get_data()
    page = data['parking_page']

    kb = [
        [InlineKeyboardButton(text="Выбрать место", callback_data=f"parking_{parking_id}")],
        [
            InlineKeyboardButton(text="⬅", callback_data="back_parking_page"),
            InlineKeyboardButton(text="{}/{}".format(page, count), callback_data='just_page'),
            InlineKeyboardButton(text="➡", callback_data="next_parking_page")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=kb)
