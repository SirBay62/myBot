from aiogram import Bot, Dispatcher

bot = Bot(token='')
dp = Dispatcher(bot)

async def main():
    await db.start_polling(bot)