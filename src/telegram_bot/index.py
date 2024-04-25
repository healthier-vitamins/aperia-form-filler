import asyncio
from telegram import Bot
from telegram.ext import Application
from telegram import Update

from dotenv import load_dotenv
import os

load_dotenv()


async def main():
    telegram_env = os.getenv("TELEGRAM_TOKEN")
    bot = telegram(telegram_env)
    async with bot:
        print(await bot.get_me())


if __name__ == "__main__":
    asyncio.run(main())
