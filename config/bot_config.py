import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
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
