__all__ = ['register_my_bookings_commands']

from aiogram import Router, F

from handlers.my_books.my_books import my_books
from handlers.my_books.paginator.next_booking_page import next_booking_page
from handlers.my_books.paginator.back_booking_page import back_booking_page
from handlers.my_books.enter_my_booking import enter_my_booking

from handlers.my_books.booking_actions import booking_pay, help_route, cancel_booking, successful_payment
from handlers.my_books.back_to_my_booking import back_to_my_booking


def register_my_bookings_commands(router: Router):
    router.callback_query.register(my_books, F.data == "my_booking")
    router.callback_query.register(next_booking_page, F.data == "next_booking_page")
    router.callback_query.register(back_booking_page, F.data == 'back_booking_page')
    router.callback_query.register(enter_my_booking, lambda query: query.data.startswith('booking_'))

    router.callback_query.register(booking_pay, F.data == 'booking-pay')
    router.message.register(successful_payment, F.content_type == 'successful_payment')

    router.callback_query.register(help_route, F.data == 'help_route')
    router.callback_query.register(cancel_booking, F.data == 'cancel_booking')
    router.callback_query.register(back_to_my_booking, F.data == 'back_to_my_booking')
