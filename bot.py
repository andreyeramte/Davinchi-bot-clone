from asyncio
from aiogram import Bot, Dispatcher 

import handlers  
from data.DataBase import DataBase
from config_reader import config 

async def main() -> None: 
    bot = Bot(config.bot_token.get_secret_value(7056574891:AAG0Tv1kDAegeiZgWBZWk2xUF4LcqAsy_cY))
    db = Dispatcher()
    db = DataBase("users_db.db, "users")

    #await db.create_table
    db.include_routers
    handlers.questionare.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, db=db)

if __name__ == "__main__":
    asyncio.run(main())
    

    