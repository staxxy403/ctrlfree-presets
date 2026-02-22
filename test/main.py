from dotenv import load_dotenv
load_dotenv()

import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

CUSTOM_WELCOME = os.getenv("WELCOME_MSG", "Привет! Я тестовый Эхо-бот.")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text == '/start')
async def cmd_start(message: types.Message):
    await message.answer(CUSTOM_WELCOME)

@dp.message()
async def echo_handler(message: types.Message):
    await message.send_copy(chat_id=message.chat.id)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())