import asyncio
import telegram
from telegram.ext import Application
from telegram import Update

from dotenv import load_dotenv
import os

load_dotenv()


async def main():
    telegram_env = os.getenv("TELEGRAM_TOKEN")
    bot = telegram.Bot(telegram_env or '')
    async with bot:
        print(await bot.get_me())


if __name__ == "__main__":
    asyncio.run(main())
