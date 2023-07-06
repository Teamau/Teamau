from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

import os

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Bot started!')

def main():
    updater = Updater(BOT_TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
