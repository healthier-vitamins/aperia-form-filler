# Description
Telegram bot to automatically fill up a form with Python selenium to enter NTT office.

This program helps automate the process down to a single tap through Telegram.

## Demonstration 
[Video](https://drive.google.com/file/d/19Dr329uSgGysXI9vFfVvPMJFeHDJqTyY/view?usp=drive_link)

# Operate the bot
I run the script on my computer through task scheduler at 8.30am.

Next I send a command `send_qr` through my telegram bot. The script then opens the link and fills up the form with python selenium on my computer.

Within the task scheduler, I set it to stop running the event after 4 hours, which automatically stops the bot from running to conserve resources.

Alternatively, if running the telegram bot on the computer manually, you may also send `stop_polling` command to stop the telegram bot remotely.

# Logs
Logs are compiled within a file, labelled and saved on a per-day basis for debugging purposes.
