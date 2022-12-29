from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.client_kb import stop_markup
from config import ADMINS
from config import bot
from database import db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private' and message.from_user.id in ADMINS:
        await FSMAdmin.photo.set()
        await message.answer(f"Hello {message.from_user.first_name} Send photo of bludo",
                             reply_markup=stop_markup)
    else:
        await message.answer('tolko admins')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer('Name of bludo:')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer('Opishi bludo')


async def load_desc(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['desc'] = message.text
    await FSMAdmin.next()
    await message.answer('How much?')


async def load_cost(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cost'] = f'{message.text}$'
        await bot.send_photo(message.from_user.id, data['photo'],
                             caption=f"{data['name']} ,"
                                     f"{data['desc']} ,"
                                     f"{data['cost']}")

    await db.sql_command_insert(state)
    await state.finish()
    await message.answer('Finish!')


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer('Otminet')


async def delete_data(message: types.Message):
    foods = await db.sql_command_all()
    for eda in foods:
        await bot.send_photo(message.from_user.id, eda[1],
                             caption=f"Name: {eda[2]}\n"
                                     f"Description: {eda[3]}\n"
                                     f"price: {eda[4]}\n",
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(
                                     f'Delete {eda[2]}',
                                     callback_data=f'delete {eda[2]}'
                                 ))
                                )


async def complete_delete(call: types.CallbackQuery):
    await db.sql_command_delete(call.data.replace('delete ', ''))
    await call.answer(text='Deleted from database', show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_registration,
                                Text(equals='stop', ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo, content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_desc, state=FSMAdmin.description)
    dp.register_message_handler(load_cost, state=FSMAdmin.price)
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith('delete '))