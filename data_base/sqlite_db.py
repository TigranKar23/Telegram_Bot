import sqlite3 as sq
from create_bot import dp, bot

def sql_start():
    global base, cur
    base = sq.connect('test1.db')
    cur = base.cursor()
    if base:
        print('Database is connected OK')
        base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
        base.commit()

async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def open_menu(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
      

        try:
            await bot.send_photo(message.from_user.id, ret[0],f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[3]}')
        except Exception as e:
            print(f"Ошибка при отправке фотографии для {ret[1]}: {e}")

def sql_delete_product(name):
    conn = sq.connect('test1.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM menu WHERE name=?", (name,))
    conn.commit()
    conn.close()