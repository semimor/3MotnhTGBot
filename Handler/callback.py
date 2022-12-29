from config import bot
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Next",callback_data="button_call_2")
    markup.add(button_call_2)
    question = "The GOAT?"
    answer = [
        "Patrick Beverley",
        "Ben Simmons",
        "Micael Jerkin",
        "LeFool Trasheyms"
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=1,
        explanation="Can you feel the dark?",
        open_period=60,
        reply_markup=markup
    )

async def quiz3(call: types.CallbackQuery):
    question = "How should a dog wear pants?"
    answer = [
        "Number one",
        "Number two",
        "I dont know",
        "Why you asking that?"
]
    photo = open('media/alexa.jpg' , 'rb')

    await bot.send_photo(call.from_user.id , photo)

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=True,
        type='quiz',
        correct_option_id=3,
        explanation="Stupid MF",
        open_period=60
    )




def register_callback_handler(dp: Dispatcher):
    dp.register_callback_query_handler(quiz2,  lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(quiz3, text = "button_call_2")