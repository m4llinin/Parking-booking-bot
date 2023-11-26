from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
import utils.db_api.db_commands as commands
from keyboards.booking_actions import booking_actions_kb
from lexicon.lexicon_ru import lexicon


async def enter_my_booking(callback: CallbackQuery, state: FSMContext):
    booking_id = int(callback.data.split('_')[1])
    booking = await commands.select_booking_by_id(booking_id)
    await state.update_data(booking_id=booking_id)
    await state.update_data(status=booking.status)
    await state.update_data(last_message=callback.message)
    status = 'Ожидание оплаты' if booking.status == 'waiting' else 'Оплачено'
    await callback.message.edit_text(text=lexicon['booking_info'].format(
        booking.id_parking, booking.vehicle_number, f'{booking.start_date} {booking.start_time}',
        f'{booking.end_date} {booking.end_time}', status), parse_mode='HTML',
        reply_markup=await booking_actions_kb(state))
