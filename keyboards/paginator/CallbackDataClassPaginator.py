from aiogram.filters.callback_data import CallbackData


class Parking(CallbackData, prefix="parking"):
    id: int


class Booking(CallbackData, prefix="booking"):
    id: int
