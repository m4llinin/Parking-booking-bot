__all__ = ['start', 'register_user_commands']

from aiogram import Router
from aiogram.filters import CommandStart

from handlers.start import start


def register_user_commands(router: Router):
    router.message.register(start, CommandStart())
