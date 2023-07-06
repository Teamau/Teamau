import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

load_dotenv()

TOKEN = os.getenv('BOT_TOKEN')
SAVE_DIR = '/path/to/save/directory'
CHANNEL_ID = os.getenv('CHANNEL_ID')
SERVER_PORT = os.getenv('SERVER_PORT')

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(update: Update, context):
    """Send a welcome message when the command /start is issued."""
    update.message.reply_text('Welcome to the File Storage Bot! Send me any file, and I will save it for you.')


def save_file(update: Update, context):
    """Save the file sent by the user and share the link to the channel."""
    file = update.message.document
    file_id = file.file_id
    file_name = file.file_name

    # Download the file
    new_file = context.bot.get_file(file_id)
    new_file.download(f'{SAVE_DIR}/{file_name}')

    # Generate the file link
    server_host = os.environ.get('HOSTNAME', 'localhost')
    file_link = f'https://{server_host}:{SERVER_PORT}/files/{file_name}'

    # Share the link to the channel
    context.bot.send_message(chat_id=CHANNEL_ID, text=f'New file uploaded: [{file_name}]({file_link})',
                             parse_mode='Markdown')

    update.message.reply_text('File saved successfully!')


def create_link(update: Update, context):
    """Generate a link to add the bot to the channel and send it to the channel."""
    bot_username = context.bot.username
    link = f'https://t.me/{bot_username}?startgroup=new'  # Link to add the bot to the channel as an administrator

    # Send the link to the channel
    context.bot.send_message(chat_id=CHANNEL_ID, text=f'Click the link to add the bot to the channel: {link}')

    update.message.reply_text('Link sent to the channel!')


def error(update: Update, context):
    """Log errors caused by updates."""
    logger.warning(f'Update {update} caused error {context.error}')


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("createlink", create_link))

    # Register message handler for files
    dp.add_handler(MessageHandler(Filters.document, save_file))

    # Log all errors
    dp.add_error_handler(error)

    # Start the bot
    updater.start_polling()
    logger.info('Bot started!')

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM, or SIGABRT.
    updater.idle()


if __name__ == '__main__':
    main()
