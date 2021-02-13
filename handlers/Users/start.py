from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp, db
import sqlite3


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    try:
        db.add_users(id=message.from_user.id, name=name)
    except sqlite3.IntegrityError as err:
        print(err)

    count_users = db.count_users()[0]
    await message.answer(
        "\n" . join([
            f'Саламатсызбы, {message.from_user.full_name}!',
            'Сурооңузду бериңиз.',

        ])
    )
    #f'V baze <b>{count_users}</b> polzovatelei'