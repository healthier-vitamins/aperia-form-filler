To enter the NTT office in Aperia, a form needs to be filled which sends an SMS containing a QR code to scan at the gantry.

This program helps automate the process down to a single tap through telegram.

I run the script on my computer through task scheduler at 8.30am.

Next I send a command `send_qr` through my telegram bot. The script then opens the link and fills up the form with python selenium on my computer.

Within the task scheduler, I set it to stop running the event after 4 hours, which automatically stops the bot from running to conserve resources.

Alternatively, if running the telegram bot on the computer manually, you may also send `stop_polling` command to stop the telegram bot remotely.

Logs are compiled within a file, labelled and saved on a per-day basis for debugging purposes.
