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
def tarix(update, context):
    keyboard = [
        ['Abulfayzxon 📖'],
        ['Akbarnoma 📚'],
        ['Qobusnoma 📚'],
        ['Ortga 🔙']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False)
    update.message.reply_text('Tarixni tanlang:', reply_markup=reply_markup)

def matematika(update, context):
    keyboard = [
        ['Axborotnoma 📘'],
        ['Oliy matematika asoslari 📙'],
        ['Differensial tenglamalar 📒'],
        ['Ortga 🔙']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False)
    update.message.reply_text('Matematika kitoblaridan tanlang:', reply_markup=reply_markup)

def it(update, context):
    keyboard = [
        ['Python 🐍'],
        ['JavaScript asoslari 🌐'],
        ['HTML-CSS 🌍'],
        ['Ortga 🔙']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False)
    update.message.reply_text('IT kitoblaridan birini tanlang:', reply_markup=reply_markup)

def english(update, context):
    keyboard = [
        ['The Great Gatsby 📖'],
        ['Pride and Prejudice 📚'],
        ['To Kill a Mockingbird 📚'],
        ['Ortga 🔙']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False)
    update.message.reply_text('English kitoblaridan birini tanlang:', reply_markup=reply_markup)

def russian(update, context):
    keyboard = [
        ['Зеленая миля 📖'],
        ['Книжный вор 📚'],
        ['Гарри Поттер и Кубок огня 📘'],
        ['Ortga 🔙']
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=False)
    update.message.reply_text('Русский kitoblaridan birini tanlang:', reply_markup=reply_markup)

def back_(update, context):
    start(update, context)  

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
tarix_handler = MessageHandler(Filters.regex('Tarix 📜'), tarix)
matematika_handler = MessageHandler(Filters.regex('Matematika 📐'), matematika)
it_handler = MessageHandler(Filters.regex('IT 💻'), it)
english_handler = MessageHandler(Filters.regex('English 🇬🇧'), english)
russian_handler = MessageHandler(Filters.regex('Русский 🇷🇺'), russian)
back_handler = MessageHandler(Filters.regex('Ortga 🔙'), back_)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(tarix_handler)
dispatcher.add_handler(matematika_handler)
dispatcher.add_handler(it_handler)
dispatcher.add_handler(english_handler)
dispatcher.add_handler(russian_handler)
dispatcher.add_handler(back_handler)

updater.start_polling() 
updater.idle()
