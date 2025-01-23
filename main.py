import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

TOKEN = os.environ.get('TOKEN')  

def start(update, context):
    keyboard = [
        ['Tarix 📜'],
        ['Matematika 📐'],
        ['IT 💻'],
        ['English 🇬🇧'],
        ['Русский 🇷🇺']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False)
    update.message.reply_text('Xush kelibsiz!', reply_markup=reply_markup)
updater=Updater(TOKEN, use_context=True)
dispatcher=updater.dispatcher
start_handler=CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()
updater.idle()