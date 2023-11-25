import asyncio

from aiogram.types import BotCommand

from config.bot_config import dp, bot
from handlers import register_user_commands
from handlers.make_booking import register_make_booking_commands
from handlers.my_books import register_my_bookings_commands
from utils.dp_api.db_gino import on_startup, db
import utils.dp_api.db_commands as commands
import random


async def main():
    # подключение к бд
    await on_startup(db)

    # удаление данных
    # await db.gino.drop_all()

    # создание таблиц
    # await db.gino.create()

    bot_commands = (
        ("start", "Начало работы с ботом"),
    )

    # Cоздание тестовых парковок
    # await commands.add_parking(40, 60, 150, [random.randint(0, 1) for _ in range(150)])
    # await commands.add_parking(39, 63, 100, [random.randint(0, 1) for _ in range(100)])
    # await commands.add_parking(20, 50, 20, [random.randint(0, 1) for _ in range(20)])
    # await commands.add_parking(73, 55, 70, [random.randint(0, 1) for _ in range(70)])

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)
    register_make_booking_commands(dp)
    register_my_bookings_commands(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")
