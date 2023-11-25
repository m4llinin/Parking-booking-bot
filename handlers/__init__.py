__all__ = ['start', 'register_user_commands']

from aiogram import Router, F
from aiogram.filters import CommandStart

from handlers.start import start
from handlers.just_page import just_page


def register_user_commands(router: Router):
    router.message.register(start, CommandStart())
    router.callback_query.register(just_page, F.data == "just_page")
