from aiogram.fsm.context import FSMContext
from lexicon.lexicon_ru import lexicon
from keyboards.paginator.booking_paginator import create_booking_paginator_keyboard

from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Invoice, LabeledPrice
import utils.db_api.db_commands as commands


async def booking_pay(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    await callback.message.answer_invoice(
        title="Оплата парковки",
        description="Оплата брони парковочного места",
        provider_token='1744374395:TEST:7931d38eb15aa37e4b26',
        currency="rub",
        photo_url="https://cdn.iconscout.com/icon/premium/png-512-thumb/pay-parking-2607820-2181787.png?f=webp&w=256",
        is_flexible=True,
        photo_width=256,
        photo_height=256,
        prices=[LabeledPrice(label='Парковка', amount=3000)],
        payload="test-invoice-payload", )


async def help_route(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    booking = await commands.select_booking_by_id(data['booking_id'])
    cur_parking = await commands.select_parking(booking.id_parking)
    await callback.message.answer_location(cur_parking.latitude, cur_parking.longitude)
    await callback.message.answer(text=lexicon['help_route'],
                                  reply_markup=InlineKeyboardMarkup(
                                      inline_keyboard=[
                                          [InlineKeyboardButton(text='Назад', callback_data='my_booking')]]))


async def cancel_booking(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    await commands.delete_booking(data['booking_id'])
    await callback.answer(text=lexicon['cancel_booking'])
    await callback.message.edit_text(text="Вы вернулись в список броней",
                                     reply_markup=await create_booking_paginator_keyboard(state))
