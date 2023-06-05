from config import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
import buttons
import to_json

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
import json, string, os
from create_bot import dp
from data_base import sqlite_db

async def on_startup(_):
    print('Program start')
    sqlite_db.sql_start()

from handlers import client, admin, other

client.register_handlers_client(dp)
admin.register_handlers_client(dp)
other.register_handlers_client(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)