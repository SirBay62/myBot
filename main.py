import asyncio
from aiogram import Bot, Dispatcher

bot = Bot(token='8153480092:AAFjypyPyk76mAowNHGTIIN4gv3VKOmbBNE')
dp = Dispatcher(bot)

async def main():
    await db.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())