from aiogram import Router, F
from aiogram.types import Messages

router = Router()
@router.message(F.text.casefold())
async def echo(message: Message) -> None:
    if message.text == "Моя анкета":
        ...

