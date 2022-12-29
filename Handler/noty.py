import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="okey!")

async def meet_w_Esen():
    await bot.send_message(chat_id=chat_id, text="lets go to lesson my n-word" )

async def scheduleres():
    aioschedule.every().saturday.at("23:41").do(meet_w_Esen)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)

def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'noty' in word.text)