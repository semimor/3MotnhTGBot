from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

stop_keyboard = KeyboardButton('STOP')
stop_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True
).add(stop_keyboard)