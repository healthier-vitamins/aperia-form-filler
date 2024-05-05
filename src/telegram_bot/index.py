from dotenv import load_dotenv
import os

load_dotenv()

import logging

logger = logging.getLogger(__name__)

from datetime import datetime

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

import subprocess
import sys

# format the current date and time
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

token = os.getenv("TELEGRAM_TOKEN")
if not token:
    raise Exception("Token missing.")

application = ApplicationBuilder().token(token).build()

# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot

# logging config (python default logging library)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    # filename=f"aperia-form-filler_{timestamp}.log",
    # encoding="utf-8",
)


async def send_qr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ? exec: only used when there's a need to share variables to the other file
    # file_path = "../index.py"
    # with open(file_path, "r") as file:
    #     code = file.read()
    #     exec(code)

    # python's default library to execute other python files
    try:
        file_path = "./src/selenium/index.py"
        result = subprocess.run(
            [sys.executable, file_path], capture_output=True, text=True
        )
        if update.message:

            if result.returncode == 0:
                await update.message.reply_text("qr code script executed successfully")
                logging.info("successfully executed")
            else:
                await update.message.reply_text("qr code script failed :(")
                logging.error(result.stderr)

    except Exception as err:
        if update.message:
            await update.message.reply_text(
                "qr code script failed due to an exception :("
            )
            logging.error(err)


async def stop_polling(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("stopping bot")
    try:

        #! does not work
        # context.bot_data["updater"].stop()

        # #! does not work
        # token = os.getenv("TELEGRAM_TOKEN")
        # if not token:
        #     raise Exception("Token missing.")
        # application = ApplicationBuilder().token(token).build()

        application.stop_running()
        # await application.shutdown()
        # raise KeyboardInterrupt("Stopped bot")

    except Exception as err:
        if update.message:
            await update.message.reply_text(
                "stop polling failed due to an exception :("
            )
        logging.error(err)
    # except KeyboardInterrupt as keyboardErr:
    #     raise KeyboardInterrupt(keyboardErr)
    finally:
        logging.shutdown()


if __name__ == "__main__":

    send_qr_handler = CommandHandler("send_qr", send_qr)
    application.add_handler(send_qr_handler)

    stop_polling_handler = CommandHandler("stop_polling", stop_polling)
    application.add_handler(stop_polling_handler)

    application.run_polling()
