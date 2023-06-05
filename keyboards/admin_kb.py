from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

button_load=KeyboardButton('/Download')
button_delete=KeyboardButton('/Delete')
button_cancel=KeyboardButton('/Cancel')
button_back=KeyboardButton('/menu')
button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_delete).add(button_cancel).add(button_back)