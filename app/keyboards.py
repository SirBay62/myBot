from aiogram.types import KeyboardButton, ReplyKeyboardMarkup,KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'),
                                     KeyboardButton(text='О нас')],
                                     ])