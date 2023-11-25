from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.paginator.selection_time import selection_time


async def next_time_page(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if data['time_page'] == 2:
        await callback.answer(text="Вы на последней странице")
        return
    await state.update_data(time_page=data['time_page'] + 1)

    await callback.message.delete()
    await callback.message.answer(text="Выберете время:", reply_markup=await selection_time(state))
