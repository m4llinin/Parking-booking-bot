from aiogram.fsm.state import State, StatesGroup


class MakeBooking(StatesGroup):
    wait_location = State()
    START_DATE = State()
    START_TIME = State()
    END_DATE = State()
    END_TIME = State()
    VEHICLE_NUMBER = State()
