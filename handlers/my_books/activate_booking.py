import base64
import io

from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
import qrcode


async def activate_booking(callback: CallbackQuery, state: FSMContext):
    data = 'Some data here'
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    image = qr.make_image(fill_color="black", back_color="white")
    image.save("qrcode.png", "PNG")

    await callback.message.answer_photo(photo='qrcode.png', reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Назад', callback_data='back_to_my_booking')]]))
