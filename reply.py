from aiogram.types import ReplyKeyboard, KeyboardButton
main = ReplyKeyboardMarkup
    keyboard=[
        [
            KeyboardButton(text="Моя анкета"),
            KeyboardButton(text="Статистика")
        ]
    ]
    resize_keyboard=True, 
    one_time_keyboard=True, 
)
