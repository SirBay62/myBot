import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

bot = Bot(token='8153480092:AAFjypyPyk76mAowNHGTIIN4gv3VKOmbBNE')
dp = Dispatcher()

@dp.message()
async def cmd_start(message: Message):
    await message.answer('Привет!')
    await message.reply('Как дела?')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())