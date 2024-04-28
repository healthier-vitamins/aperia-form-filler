import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

import os
from dotenv import load_dotenv

load_dotenv()

import subprocess
import sys


# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_chat:
        raise Exception("Id missing.")

    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!"
    )


async def send_qr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ? exec: only used when there's a need to share variables to the other file
    # file_path = "../index.py"
    # with open(file_path, "r") as file:
    #     code = file.read()
    #     exec(code)

    file_path = "./src/index.py"
    subprocess.run([sys.executable, file_path])


if __name__ == "__main__":
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise Exception("Token missing.")

    application = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    send_qr_handler = CommandHandler("send_qr", send_qr)
    application.add_handler(send_qr_handler)

    application.run_polling()
