from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Календарь"),
            KeyboardButton(text="Состав")
        ],
        [
            KeyboardButton(text="Статистика"),
            KeyboardButton(text="Help"),
        ],
    ],
    resize_keyboard=True
)