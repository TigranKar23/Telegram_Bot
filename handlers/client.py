from aiogram import Bot, Dispatcher, executor, types
import buttons
from keyboards import kb_client
from data_base import sqlite_db
from create_bot import dp, bot

import json, string

# @dp.message_handler(commands=['start'])
async def process_hello(message: types.Message):
    # await message.answer('Hello', reply_markup=buttons.mainmenu)
    await bot.send_message(message.from_user.id, 'Hello', reply_markup=kb_client)
    # await bot.send_message(message.from_user.id, message.from_user)

# @dp.message_handler(commands=['menu'])
async def menu_command(message: types.Message):
    await sqlite_db.open_menu(message)
    
# @dp.message_handler()
# async def menu(message: types.Message):

#     try:
#         if {i.lower().translate(str.maketrans('', '', string.punctuation )) for i in message.text.split(' ')}\
#                 .intersection(set(json.load(open('cenz.json')))) != set():
#                 await message.reply('Wrong')
#                 await message.delete()
#         match message.text:
#             case "О нас":
#                 await message.reply('AAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
#             case "Помошь":
#                 await message.reply('BBBBBBBBBBBBBBBBBBBBBBBBBBBBB', reply_markup=buttons.help)
#             case _:
#                 pass
#     except Exception as e:
#         print(e)

# @dp.message_handler()
# async def help_menu(call: types.CallbackQuery):
#     match call.data:
#         case "helpfinance":
#             await call.message.answer("FFFFIIIIINNNAAANNNSSEEE")
#         case "helpfisical":
#             await call.message.answer('FFFIIIISSSIIIICCCAAAALLL')

# @dp.message_handler(commands=['start'])
# async def process_hello(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Hiii \n Whats ap bro')


# @dp.message_handler()
# async def process_helloo(message: types.Message):
#     try:
#         match message.text:
#             case "О нас":
#                 await message.reply('AAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
#             case "Помошь":
#                 await message.reply('BBBBBBBBBBBBBBBBBBBBBBBBBBBBB', reply_markup=buttons.help)
#             case _:
#                 pass
#     except Exception as e:
#         print(e)



# @dp.message_handler()
# async def process_helloo(message: types.Message):
#     if {i.lower().translate(str.maketrans('', '', string.punctuation )) for i in message.text.split(' ')}\
#         .intersection(set(json.load(open('cenz.json')))) != set():
#         await message.reply('Wrong')
#         await message.delete()



# @dp.message_handler()
# async def process_helloo(message: types.Message):
#     if (message.text == 'О нас'):
#         await message.reply('AAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
#     elif(message.text == 'Помошь'):
#         await message.reply('BBBBBBBBBBBBBBBBBBBBBBBBBBBBB', reply_markup=buttons.help)
#     if {i.lower().translate(str.maketrans('', '', string.punctuation )) for i in message.text.split(' ')}\
#         .intersection(set(json.load(open('cenz.json')))) != set():
#         await message.reply('Wrong')
#         await message.delete()



# @dp.message_handler(commands=['help'])
# async def process_reply(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Can i help you ?')



# @dp.message_handler()
# async def process_help(message: types.Message):
#     if message.text == 'hi':
#         await message.answer('hii bro')
#     else:
#             await message.reply('Your send message')



# @dp.message_handler()
# async def process_help(message: types.Message):
#     await message.answer(message.text)

def register_handlers_client(dp : Dispatcher):
    # բոլոր ֆունկցիաները գրանցում ենք այստեղ (register_message_handler ---> ֆունկցիաները մի տեղ հավաքելու համար ֆունկցիա)
    dp.register_message_handler(process_hello, commands=['start', 'help'])
    dp.register_message_handler(menu_command, commands=['menu'])
    # dp.register_message_handler(menu)
    # dp.register_message_handler(help_menu)