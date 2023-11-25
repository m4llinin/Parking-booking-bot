from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime
from utils.dp_api.db_commands import add_booking


def check_vehicle_number(number: str):
    right_sym = ['А', 'В', 'Е', 'К', 'М', 'Н', 'О', 'Р', 'С', 'Т', 'У', 'Х']
    num = [str(i) for i in range(10)]
    if number[0] in right_sym and number[4] in right_sym and number[5] in right_sym and number[1] in num \
            and number[2] in num and number[3] in num and number[6] in num and number[7] in num:
        return True
    return False


async def accept_vehicle_number(message: Message, state: FSMContext):
    text = message.text
    if check_vehicle_number(text):
        data = await state.get_data()
        await add_booking(
            id_parking=data["parking"],
            user_id=message.from_user.id,
            vehicle_number=text,
            start_date=data['start_date'],
            start_time=datetime.strptime(data['start_time'], "%H:%M"),
            end_date=data['end_date'],
            end_time=datetime.strptime(data['end_time'], "%H:%M")
        )
        button = InlineKeyboardButton(
            text="В главное меню", callback_data="back_to_main"
        )
        keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
        await state.clear()
        await state.update_data(parking_page=1, booking_page=1, user_id=message.from_user.id)
        await message.answer(text="Ваша бронь успешно создана, приезжайте вовремя", reply_markup=keyboard)
    else:
        await message.answer(text="Номер автомобился отправлен неправильно")
