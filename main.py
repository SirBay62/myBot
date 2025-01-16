import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

bot = Bot(token='8153480092:AAFjypyPyk76mAowNHGTIIN4gv3VKOmbBNE')
dp = Dispatcher()

# @dp.message()
# async def cmd_start(message: Message):
#     await message.answer('Привет!')
#     await message.reply('Как дела?')

@dp.message(CommandStart())
async def cmd_name(message: Message):
    await message.reply("Привет! Давай поработаем.")

# @dp.message(Command(BotCommand(command="привет")))
@dp.message(Command("имя"))
@dp.message(F.text.casefold() == "имя")
async def on_name(message: Message):
    await message.answer('Меня зовут AlexBot')

@dp.message(F.text)
async def on_name(message: Message):
    await message.answer('Неизвестная команда')

# @dp.message()
# async def cmd_start(message: Message):
#     await message.answer('Неизвестная команда!')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())