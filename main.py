import asyncio

from aiogram import types

import config
import logging

from aiogram.types.message import ContentType

from aiogram.types import BotCommand

from config.bot_config import dp, bot, PAYMENTS_TOKEN
from handlers import register_user_commands
from handlers.make_booking import register_make_booking_commands
from utils.dp_api.db_gino import on_startup, db
import utils.dp_api.db_commands as commands
import random


async def main():
    # подключение к бд
    await on_startup(db)

    # удаление данных
    await db.gino.drop_all()

    # создание таблиц
    await db.gino.create()

    bot_commands = (
        ("start", "Начало работы с ботом"),
    )

    # Cоздание тестовых парковок
    await commands.add_parking(40, 60, 150, [random.randint(0, 1) for _ in range(150)])
    await commands.add_parking(39, 63, 100, [random.randint(0, 1) for _ in range(100)])
    await commands.add_parking(20, 50, 20, [random.randint(0, 1) for _ in range(20)])
    await commands.add_parking(73, 55, 70, [random.randint(0, 1) for _ in range(70)])

    commands_for_bot = []
    for cmd in bot_commands:
        commands_for_bot.append(BotCommand(command=cmd[0], description=cmd[1]))
    await bot.set_my_commands(commands=commands_for_bot)

    register_user_commands(dp)
    register_make_booking_commands(dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("Bot stopped")

logging.basicConfig(level=logging.INFO)

PRICE = types.LabeledPrice(label="Подписка на 1 месяц", amount=500 * 100)  # в копейках (руб)


@dp.message_handler(commands=['buy'])
async def buy(message: types.Message):
    if PAYMENTS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!!!")

    await bot.send_invoice(message.chat.id,
                           title="Подписка на бота",
                           description="Активация подписки на бота на 1 месяц",
                           provider_token=PAYMENTS_TOKEN,
                           currency="rub",
                           photo_url="https://www.aroged.com/wp-content/uploads/2022/06/Telegram-has-a-premium-subscription.jpg",
                           photo_width=416,
                           photo_height=234,
                           photo_size=416,
                           is_flexible=False,
                           prices=[PRICE],
                           start_parameter="one-month-subscription",
                           payload="test-invoice-payload")


# pre checkout  (must be answered in 10 seconds)
@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)


# successful payment
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    print("SUCCESSFUL PAYMENT:")
    payment_info = message.successful_payment.to_python()
    for k, v in payment_info.items():
        print(f"{k} = {v}")

    await bot.send_message(message.chat.id,
                           f"Платеж на сумму {message.successful_payment.total_amount // 100} {message.successful_payment.currency} прошел успешно!!!")
