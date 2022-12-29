import random
import sqlite3
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.db')
    cursor = db.cursor()
    if db:
        print('DataBase was created')
    db.execute("CREATE TABLE IF NOT EXISTS menu "
               "(id INTEGER, "
               "photo TEXT, "
               "name TEXT PRIMARY KEY, "
               "description TEXT, "
               "price TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO menu VALUES (?, ?, ?, ?, ?)',
                       tuple(data.values()))
    db.commit()


async def sql_command_random(message):
    result = cursor.execute('SELECT * FROM menu').fetchall()
    random_user = random.choice(result)
    await bot.send_photo(message.from_user.id, random_user[1], caption=f"Name: {random_user[2]}\n"
                                                                      f"Description: {random_user[3]}\n"
                                                                    f"price: {random_user[4]}\n")


async def sql_command_all():
    return cursor.execute('SELECT * FROM menu')


async def sql_command_delete(name):
    cursor.execute('DELETE FROM menu WHERE name == ?', (name, ))
    db.commit()