import os
import logging
from telegram.ext import Updater, CommandHandler

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Define your Telegram bot token
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# Define the directory where the files will be stored
FILE_DIRECTORY = 'file_storage'

# Define the ID of the channel to send the links
CHANNEL_ID = 'YOUR_CHANNEL_ID'

# Create the file storage directory if it doesn't exist
if not os.path.exists(FILE_DIRECTORY):
    os.makedirs(FILE_DIRECTORY)

# Handler for the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to the file sharing bot!")

# Handler for the /share command
def share_file(update, context):
    # Check if a file was sent
    if 'document' not in update.message.effective_attachment:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Please send a file to share.")
        return

    # Get the file object
    file_object = context.bot.get_file(update.message.effective_attachment['document'].file_id)

    # Save the file
    file_path = os.path.join(FILE_DIRECTORY, update.message.effective_attachment['document'].file_name)
    file_object.download(file_path)

    # Send the download link to the user
    download_link = f"https://yourdomain.com/{file_path}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"File shared successfully!\n\nDownload link: {download_link}")

    # Send the download link to the specific channel
    context.bot.send_message(chat_id=CHANNEL_ID, text=f"New file shared!\n\nDownload link: {download_link}")

# Create an Updater object and attach the bot token
updater = Updater(token=TOKEN, use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register the command handlers
start_handler = CommandHandler('start', start)
share_handler = CommandHandler('share', share_file)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(share_handler)

# Start the bot
updater.start_polling()￼Enter
