from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Menu')
b2 = KeyboardButton('/Режим работы')
b3 = KeyboardButton('/About')
b4 = KeyboardButton('/Contact', request_contact=True)
b5 = KeyboardButton('/Location', request_location=True)
b6 = KeyboardButton('/Dashboard')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).add(b3).row(b4, b5, b6)