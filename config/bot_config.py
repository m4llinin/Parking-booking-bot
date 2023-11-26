import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
import logging

load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

IP = os.getenv('IP')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')
DATABASE = os.getenv('DATABASE')

POSTGRES_URI = F'postgresql://{PGUSER}:{PGPASSWORD}@{IP}/{DATABASE}'

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


# pre checkout  (must be answered in 10 seconds)
@dp.pre_checkout_query(lambda query: True)
async def pre_checkout_query(pre_checkout_q: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_q.id, ok=True)
