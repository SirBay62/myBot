import asyncio
from aiogram import Bot, Dispatcher, F
from app.handlers import router


async def main():
    bot = Bot(token='8153480092:AAFjypyPyk76mAowNHGTIIN4gv3VKOmbBNE')
    dp = Dispatcher()
    dp.include_routers(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')