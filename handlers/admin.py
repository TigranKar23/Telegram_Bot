from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot
from aiogram import types, Dispatcher, executor
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
import openai
from parser import parser
import logging
import aiohttp
import requests
#im@
openai.api_key = "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"
FACEBOOK_TOKEN = 'EAAEZAwt7E4QUBOZChvJVYHrRbZC2iOsqCBn2K8q99HBNs8EVZCDvPjwynphw5hV1ZAoU0W5cLQTOvZCOLdC12o1p6NWZBDETYNZC3XiFMZBaxL2JbG6xnXjbjDozZC9tHVWMTd8dRPNohbheKbRQxoEgoFYwykMcaEFyKYD8HVovTfw2ZCQ8i90rmaNNKEOp6otzEONknlg8vhjbQ2E5JpJckh8gTv1c0CKTKzZCm0OpZA3IIPX1hFQCDGyrL4gjs4OrT5XsZD'
# GROUP_ID = '114978245764679'
GROUP_ID = '4020611574659567'
#hovoin@
# openai.api_key = "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"

ID = None
logging.basicConfig(level=logging.INFO)

class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()

class DeleteState(StatesGroup):
    name = State()

class SearchState(StatesGroup):
    search_data = State()

# @dp.message_handler(commands="Download", is_chat_admin=True)
# async def make_changes_comand(message:types.Message):
#     global ID
#     ID=message.from_user.id
#     await bot.send_message(message.from_user.id,'You are Admin')
#     await message.delete()

def split_message(text, length=4096):
    return [text[i:i+length] for i in range(0, len(text), length)]

# @dp.message_handler(commands=['get'])
async def get_khl_data(message: types.Message):
    data = parser.parser()
    for player_info in data:
        player_text = "\n".join([f"{key}: {value}" for key, value in player_info.items()])
        await message.reply(player_text)

# ------------------------------FACEBOOK-------------------------------------

# @dp.message_handler(commands=['facebook'])
async def facebook_data(message: types.Message):
    data = await get_facebook_data()
    await message.answer(f"Facebook Data: {data}")

async def get_facebook_data():
    # url = f"https://graph.facebook.com/v13.0/me?fields=id,name&access_token={FACEBOOK_TOKEN}"
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(url) as response:
    #         return await response.json()
    # url = f"https://graph.facebook.com/me?fields=id,name,email&access_token={FACEBOOK_TOKEN}"

    # url = f"https://graph.facebook.com/{GROUP_ID}/feed?access_token={FACEBOOK_TOKEN}"

    # Выполнение запроса
    # response = requests.get(url)
    
    # Проверка успешности запроса
    # if response.status_code == 200:
    #     return response.json()
    # else:
    #     return f"Ошибка запроса: {response.status_code}"

    url = f"https://graph.facebook.com/{GROUP_ID}/feed?access_token={FACEBOOK_TOKEN}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()
        
# ------------------------------FACEBOOK-------------------------------------



# @dp.message_handler(commands="Delete", is_chat_admin=True)
async def delete_product(message: types.Message):
    await message.reply("Please provide the product ID you want to delete:")
    await DeleteState.name.set()


# @dp.message_handler(lambda message: message.text.isdigit(), state=None)
async def get_product_id_to_delete(message: types.Message, state:FSMContext):
    async with state.proxy() as date:
        date['name']=message.text
    data = await state.get_data()
    deleted_name = data.get("name")
    sqlite_db.sql_delete_product(deleted_name)
    await message.reply(f"Product with name <<{deleted_name}>> has been deleted.")
    await state.finish()
    
#-----------------------------------------------------------

async def beautify_text(text):
    # Capitalize the first letter
    text = text[0].upper() + text[1:]

    # Ensure the text ends with appropriate punctuation
    if not any(text.endswith(punct) for punct in ['.', '!', '?']):
        text += '.'

    return text

    # @dp.message_handler(commands="Delete", is_chat_admin=True)
async def start_search(message: types.Message):
    await message.reply("How can I assist you today?")
    await SearchState.search_data.set()


# @dp.message_handler(lambda message: message.text.isdigit(), state=None)
async def search_request(message: types.Message, state:FSMContext):
    async with state.proxy() as date:
        date['search_data']=message.text
    data = await state.get_data()
    search_data = data.get("search_data")
    # -------------------------------------------------------
    
    # response = openai.Completion.create(engine="davinci", prompt=search_data, max_tokens=150)

    try:

        response = openai.Completion.create(engine="davinci", prompt=search_data, max_tokens=150)
        text = beautify_text(response.choices[0].text.strip())
        await message.reply(text)
        await state.finish()

    except openai.error.RateLimitError:
        await message.reply("Sorry, I've exceeded my API rate limit. Please try again later.")
        await state.finish()


    # -------------------------------------------------------
    # await message.reply(response.choices[0].text.strip())
    # await message.reply(search_data)
    # await state.finish()

#-----------------------------------------------------------

# @dp.message_handler(commands="Download", state=None)
async def cm_start(message:types.Message):
    # if message.from_user.id == ID :
    if message.from_user.username == 'TigranKar23':
        await FSMAdmin.photo.set()
        await message.reply('Download Photo')

# @dp.message_handler(commands="Dashboard", state='*')
async def is_admin(message:types.Message):
    if message.from_user.username == 'TigranKar23':
        await bot.send_message(message.from_user.id, 'Start Download', reply_markup=admin_kb.button_case_admin)

# @dp.message_handler(content_types=["photo"], state=FSMAdmin.photo)
async def load_photo(message:types.Message, state:FSMContext):
    async with state.proxy() as date:
        date['photo']=message.photo[0].file_id
    await FSMAdmin.next()
    await message.reply('Name of Product')

# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message:types.Message, state:FSMContext):
    async with state.proxy() as date:
        date['name']=message.text
    await FSMAdmin.next()
    await message.reply('Description of Product')

# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message:types.Message, state:FSMContext):
    async with state.proxy() as date:
        date['description']=message.text
    await FSMAdmin.next()
    await message.reply('Price of Product')

# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message:types.Message, state:FSMContext):
    async with state.proxy() as date:
        date['price']=float(message.text)
    await sqlite_db.sql_add_command(state)
    # async with state.proxy() as date:
    # await message.reply(str(date))
    await state.finish()

# @dp.message_handler(state='*', command='Cancel')
# @dp.message_handler(Text(equals='Cancel', ignore_case=True),state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('OK')



def register_handlers_client(dp : Dispatcher):

    #delete product
    dp.register_message_handler(delete_product, commands=['Delete'])
    dp.register_message_handler(get_product_id_to_delete, state=DeleteState.name)
    

    #search
    dp.register_message_handler(start_search, commands=['search'])
    dp.register_message_handler(search_request, state=SearchState.search_data)

    dp.register_message_handler(cancel_handler, commands=['Cancel'], state='*')
    dp.register_message_handler(cancel_handler, Text(equals='Cancel', ignore_case=True), state='*')
    dp.register_message_handler(is_admin, commands=['Dashboard'], state='*')
    dp.register_message_handler(cm_start, commands=['download'], state=None)
    # dp.register_message_handler(delete_start, commands=['delete'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    # --------------------parser--------------------
    dp.register_message_handler(get_khl_data, commands=['get'], state=None)
    dp.register_message_handler(facebook_data, commands=['facebook'], state=None)
