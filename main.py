import asyncio

from aiogram.types import BotCommand

from config.bot_config import dp, bot
from handlers import register_user_commands
from utils.dp_api.db_gino import on_startup, db


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

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))
    await bot.set_my_commands(commands=commands_for_bot)
    register_user_commands(dp)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")
