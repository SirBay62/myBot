import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

bot = Bot(token='8153480092:AAFjypyPyk76mAowNHGTIIN4gv3VKOmbBNE')
dp = Dispatcher()


@dp.message()
async def cmd_start(message: Message):
    await message.answer('Привет!')
    await message.reply('Как дела?')
#
# @dp.message
# async def cmd_name(message: Message):
#     await message.reply("Привет! Я бот.")

# @dp.message_handler(commands=['start'])
# async def on_start(message: types.Message):
#     await message.answer('Привет!')
#     pass

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())