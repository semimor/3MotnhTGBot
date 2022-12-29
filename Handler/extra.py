from config import bot, ADMINS
from aiogram import types , Dispatcher

import random, time

# async def echo(message: types.message):
#     if message.text.isdigit():
#         square = int(message.text) ** 2
#         await bot.send_message(message.chat.id, square)
#     else:
#         await bot.send_message(message.chat.id, message.text)

async def game(message: types.Message):
    if not message.from_user.id in ADMINS:
        await bot.send_message(message.chat.id, "Fuck you")
    else:
        emojis = ['🎯', '🎳', '🎰', '🎲', '⚽', '️🏀']
        rand_game = random.choice(emojis)
        await bot.send_dice(message.chat.id, emoji=rand_game)

async def timeout(message: types.Message):
    ty_res = time.gmtime(int(message.text[1::]))
    res = time.strftime("%H:%M:%S", ty_res)
    if int(message.text[1::]) > 359999:
        await bot.send_message(message.from_user.id, "too many!")

    else:
        if message.text.startswith('-'):
            await bot.send_message(message.from_user.id , res)


def register_extra_game(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])
    dp.register_message_handler(timeout)
