import os

from dotenv import load_dotenv

load_dotenv()

import logging

logger = logging.getLogger(__name__)

from datetime import datetime

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Format the current date and time
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

token = os.getenv("TELEGRAM_TOKEN")
if not token:
    raise Exception("Token missing.")

# Initialise telegram application with token
application = ApplicationBuilder().token(token).build()

# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot

# Logging config (python default logging library)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename=f"aperia-form-filler_{timestamp}.log",
    encoding="utf-8",
)


async def send_qr(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # ? Exec: only used when there's a need to share variables to the other file
    # file_path = "../index.py"
    # with open(file_path, "r") as file:
    #     code = file.read()
    #     exec(code)

    # python's default library to execute other python files
    try:
        # file_path = "./src/selenium/index.py"
        # result = subprocess.run(
        #     [sys.executable, file_path], capture_output=True, text=True
        # )

        from selenium_files.main_script import execute_selenium_script

        execute_selenium_script()

        if update.message:
            await update.message.reply_text("QR code script executed successfully :)")
            logging.info("Successfully executed")

    except Exception as err:
        if update.message:
            await update.message.reply_text(
                "QR code script failed due to an exception :("
            )
            await update.message.reply_text(str(err))
            logging.error(err)


async def stop_polling(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text("Stopping bot")
    try:

        # ! Does not work
        # context.bot_data["updater"].stop()

        # ! Does not work
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
                "Failed to stop polling failed due to an exception :("
            )
            await update.message.reply_text(str(err))
        logging.error(err)
    # except KeyboardInterrupt as keyboardErr:
    #     raise KeyboardInterrupt(keyboardErr)
    finally:
        logging.shutdown()


async def heartbeat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.message:
            await update.message.reply_text("I'm alive!")
            logging.info("I'm alive!")

    except Exception as err:
        if update.message:
            await update.message.reply_text("Something went wrong getting heartbeat")
            await update.message.reply_text(str(err))
            logging.error(err)


if __name__ == "__main__":
    send_qr_handler = CommandHandler("Send_QR", send_qr)
    application.add_handler(send_qr_handler)

    stop_polling_handler = CommandHandler("Stop_Polling", stop_polling)
    application.add_handler(stop_polling_handler)

    heartbeat_handler = CommandHandler("Heartbeat", heartbeat)
    application.add_handler(heartbeat_handler)

    application.run_polling()
