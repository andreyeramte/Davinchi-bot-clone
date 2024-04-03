import asyncio
from aiogram import Bot, Dispatcher
from aiogram_reader import config
async def main() -> None: 
    bot = Bot(config.bot_token.get_secret_value(7056574891:AAG0Tv1kDAegeiZgWBZWk2xUF4LcqAsy_cY))
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    async.run(main())