_all_=['register_my_books_commands']

from aiogram import Router, F

from handlers.my_books.Back_my_books import back_my_books
from handlers.my_books.Next_my_books import next_my_books

def register_my_books_commands(router: Router):
    router.callback_query.register(back_my_books(),F.data=='back_booking_page')
    router.callback_query.register(next_my_books(), F.data == 'next_booking_page')