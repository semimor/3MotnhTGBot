from aiogram.utils import executor
from config import dp
from Handler import client, callback , extra , admin , FSMAdminMenu , noty
from database.db import sql_create
import logging

client.register_handlers_client(dp)
callback.register_callback_handler(dp)
FSMAdminMenu.register_handlers_fsm_anketa(dp)
noty.register_handlers_notification(dp)


extra.register_extra_game(dp)

async def on_startup(_):
    sql_create()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True , on_startup=on_startup)