from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext


async def create_parking_place_paginator(state: FSMContext):
    data = await state.get_data()

    page = data["parking_place_page"]
    parking_places = data['parking_places']
    count = len(parking_places) // 49 + (len(parking_places) % 49 != 0)

    kb = [[]]
    for i in range((page - 1) * 7, page * 7):
        kb.append([])
        for j in range(0, 7):
            try:
                place = parking_places[i * 7 + j]
                if not place:
                    raise IndexError
                button = InlineKeyboardButton(
                    text="{}".format(i * 7 + j+1), callback_data=f"places_{i * 7 + j}"
                )
                kb[-1].append(button)
            except IndexError:
                button = InlineKeyboardButton(
                    text="ㅤ", callback_data="just_place"
                )
                kb[-1].append(button)
        try:
            place = parking_places[i * 7]
        except IndexError:
            break
    kb.append([
        InlineKeyboardButton(text="⬅", callback_data="back_parking_places_page"),
        InlineKeyboardButton(text="{}/{}".format(page, count), callback_data='just_page'),
        InlineKeyboardButton(text="➡", callback_data="next_parking_places_page")
    ])
    return InlineKeyboardMarkup(inline_keyboard=kb)
