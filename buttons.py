from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup

mainmenu_aboutus = KeyboardButton('О нас')
mainmenu_help = KeyboardButton('Помошь')
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).row(mainmenu_aboutus, mainmenu_help)

help = InlineKeyboardMarkup(row_width=2)
help_finance = InlineKeyboardButton(text='Finance', callback_data='helpfinance')
help_fisical = InlineKeyboardButton(text='Fisical', callback_data='helpfisical')

help.insert(help_finance)
help.insert(help_fisical)