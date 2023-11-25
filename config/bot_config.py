import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
import logging


load_dotenv()
API_TOKEN = '6952792259:AAFDRY9WGl_I_3a8m7EfvlOIS-Vlyss3AH4'

IP='localhost'
PGUSER='postgres'
PGPASSWORD=''
DATABASE='parking'

POSTGRES_URI = F'postgresql://{PGUSER}:{PGPASSWORD}@{IP}/{DATABASE}'

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
