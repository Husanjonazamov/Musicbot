# aiogram import
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# kode import
from utils.env import BOT_TOKEN
import logging



logging.basicConfig(level=logging.INFO)

storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode='html')

dp = Dispatcher(bot, storage=storage)

