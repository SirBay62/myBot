from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart
from aiogram import F, Router

import app.keyboards as kb

router = Router()

# обработчик команды "старт"
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет! Давай поработаем.", reply_markup=kb.main)

# обработчик для ключевого слова и команды "имя"
@router.message(Command("имя"))
@router.message(F.text.casefold() == "имя")
async def on_name(message: Message):
    await message.answer('Меня зовут AlexBot')

# обработчик для инЛайн клавиатуры для Каталога
@router.message((F.text)=='Каталог')
async def catalog(message: Message):
    await message.answer('Выберите категорию товара', reply_markup=kb.catlog)

# обработчик выбора категории футболки
@router.callback_query(F.data == 't-shirt')
async def t_shirt(callback: CallbackQuery):
    await callback.answer('Вы выбрали категорию')
    await callback.message.answer('Вы выбрали категории футболки')

@router.message(Command('register'))
async def register(message: Message):
    await message.answer('Введите ваше имя')

# обработчик всего остального
@router.message(F.text)
async def on_other(message: Message):
    await message.answer('Неизвестная команда')


