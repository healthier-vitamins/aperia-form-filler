import asyncio
import telegram
from telegram.ext import Application
from telegram import Update

from dotenv import load_dotenv
import os

load_dotenv()

import pprint
import json


async def main():
    telegram_env = os.getenv("TELEGRAM_TOKEN")
    bot = telegram.Bot(telegram_env or "")
    async with bot:
        print(await bot.get_me())
        print("====================================================")
        updates = await bot.get_updates()
        if updates:
            for update in updates:
                print(update)
                print("====================================================")
                pprint.pprint(update)
                print("2 ====================================================")
                # print(json.dumps(update, indent=4, sort_keys=True))
                # print("3 ====================================================")
                if update.message and update.message.from_user:
                    print(update.message.from_user.id)
                    print("====================================================")
                    await bot.send_message(
                        text="hi", chat_id=update.message.from_user.id
                    )

        # print(f"updates: {updates}")
        # print(f"updates[0]: {updates[0]}")


if __name__ == "__main__":
    asyncio.run(main())
