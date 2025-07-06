
import logging
import os
import time
import requests
from telegram import Bot
from telegram.ext import CommandHandler, Updater

# Configuration
TOKEN = "7731381408:AAFHz71VdYjZm-DY0xjWJd_dDGaKQ10r4Ik"
CHAT_ID = 7336907549

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create the bot instance
bot = Bot(token=TOKEN)

def start(update, context):
    update.message.reply_text("✅ Signal bot is running... You will receive signals every 5 minutes.")

def send_signal():
    # Dummy logic for signal (can be replaced with real indicators)
    import random
    signal_type = random.choice(["BUY", "SELL"])
    pair = random.choice(["EUR/USD", "GBP/JPY"])
    signal = f"📡 5-Minute Signal
Pair: {pair}
Action: {signal_type}"
    bot.send_message(chat_id=CHAT_ID, text=signal)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()

    while True:
        send_signal()
        time.sleep(300)  # Wait 5 minutes

if __name__ == "__main__":
    main()
