__all__ = ['register_make_booking_commands']

from aiogram import Router, F
from aiogram_calendar import SimpleCalendarCallback

from handlers.make_booking.select_end_time import select_end_time
from handlers.make_booking.start_booking import start_booking
from handlers.make_booking.get_location import get_location
from handlers.make_booking.select_start_date import select_start_date
from handlers.make_booking.select_start_time import select_start_time
from handlers.make_booking.select_end_date import select_end_date
from handlers.make_booking.paginator.next_parking_page import next_parking_page
from handlers.make_booking.paginator.back_parking_page import back_parking_page
from handlers.make_booking.select_parking import select_parking
from handlers.make_booking.paginator.back_parking_places_page import back_parking_places_page
from handlers.make_booking.paginator.next_parking_places_page import next_parking_places_page
from handlers.make_booking.paginator.next_time_page import next_time_page
from handlers.make_booking.paginator.back_time_page import back_time_page
from handlers.make_booking.enter_vehicle_number import enter_vehicle_number
from handlers.make_booking.accept_vehicle_number import accept_vehicle_number
from handlers.back_to_main import back_to_main
from states.make_booking_state import MakeBooking


def register_make_booking_commands(router: Router):
    router.callback_query.register(start_booking, F.data == "to_book")
    router.message.register(get_location, F.location, MakeBooking.wait_location)
    router.callback_query.register(select_start_date, SimpleCalendarCallback.filter(), MakeBooking.START_DATE)
    router.callback_query.register(select_start_time, lambda query: query.data.startswith('time_'),
                                   MakeBooking.START_TIME)
    router.callback_query.register(select_end_date, SimpleCalendarCallback.filter(), MakeBooking.END_DATE)
    router.callback_query.register(select_end_time, lambda query: query.data.startswith('time_'),
                                   MakeBooking.END_TIME)
    router.callback_query.register(next_parking_page, F.data == "next_parking_page")
    router.callback_query.register(back_parking_page, F.data == "back_parking_page")
    router.callback_query.register(select_parking, lambda query: query.data.startswith('parking_'))

    router.callback_query.register(next_parking_places_page, F.data == "next_parking_places_page")
    router.callback_query.register(back_parking_places_page, F.data == "back_parking_places_page")

    router.callback_query.register(next_time_page, F.data == "next_time_page")
    router.callback_query.register(back_time_page, F.data == "back_time_page")

    router.callback_query.register(enter_vehicle_number, lambda query: query.data.startswith('places_'))
    router.message.register(accept_vehicle_number, F.text, MakeBooking.VEHICLE_NUMBER)
    router.callback_query.register(back_to_main, F.data == 'back_to_main')
