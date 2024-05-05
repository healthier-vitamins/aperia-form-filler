To enter my office in NTT, I need to scan a QR code and fill up a form which sends an sms containing another QR code to scan at the gantry.

This program helps automate the process with a single tap within my telegram bot.

I run the script on my computer through task scheduler at 8.30am.

Next I send a command `send_qr` through my telegram bot. The script then opens the link and fills up the form with python selenium on my computer that's running the telegram bot from task scheduler.

Finally, I'll send the last command `stop_polling` to stop the telegram bot script running on my computer to conserve resources.
