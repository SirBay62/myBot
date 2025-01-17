from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,KeyboardButton,
                           InlineKeyboardMarkup,InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=
    [
     [KeyboardButton(text='Каталог')],
     [KeyboardButton(text='Корзина')],
     [KeyboardButton(text='Контакты'),KeyboardButton(text='О нас')]
    ]
    ,resize_keyboard=True, input_field_placeholder= 'Выберите пункт меню')

catlog = InlineKeyboardMarkup(inline_keyboard=
    [
    [InlineKeyboardButton(text='Футболки', callback_data='t-shirt')],
    [InlineKeyboardButton(text='Кроссовки', callback_data='sneakers')],
    [InlineKeyboardButton(text='Кепки', callback_data='cap')],
    ])
