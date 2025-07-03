import logging
from aiogram import Bot, Dispatcher, types, executor
import os

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я бот по займам. Нажми /loan чтобы получить ссылку.")

@dp.message_handler(commands=['loan'])
async def send_loan_link(message: types.Message):
    await message.reply("Вот твоя ссылка: https://rdr.sdpdl.com.ua/in/offer/2450?aid=110933")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)