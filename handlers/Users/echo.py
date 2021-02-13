from aiogram import types
from loader import dp, db


@dp.message_handler()
async def bot_echo(message: types.Message):

    chat_id = message.from_user.id
    text = "Сиздин сурооңуз кабыл алынды. Жооп күтүңүз."

    from loader import bot

    await bot.send_message(chat_id=chat_id, text=text)

    #await message.aswer(text=text)

    mestext = message.text
    db.update_text(text=mestext, id=message.from_user.id)