import json, string
from aiogram import Bot, Dispatcher, executor, types

from create_bot import dp

# @dp.message_handler()
async def filter_message(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation )) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply('Wrong')
        await message.delete()

def register_handlers_client(dp : Dispatcher):
    # բոլոր ֆունկցիաները գրանցում ենք այստեղ (register_message_handler ---> ֆունկցիաները մի տեղ հավաքելու համար ֆունկցիա)
    dp.register_message_handler(filter_message)