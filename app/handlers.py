from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from aiogram import F, Router

router = Router()

# обработчик команды "старт"
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply("Привет! Давай поработаем.")

# обработчик для ключевого слова и команды "имя"
@router.message(Command("имя"))
@router.message(F.text.casefold() == "имя")
async def on_name(message: Message):
    await message.answer('Меня зовут AlexBot')

# обработчик всего остального
@router.message(F.text)
async def on_other(message: Message):
    await message.answer('Неизвестная команда')
