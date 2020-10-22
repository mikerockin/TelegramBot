from telegram import ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from telegram.ext import MessageHandler
from settings import TG_TOKEN, TG_API_URL
import requests
from bs4 import BeautifulSoup



def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?')
    my_keyboard = ReplyKeyboardMarkup([['Анекдот', 'начать']], resize_keyboard=True)
    bot.message.reply_text('Приветствую тебя о , {}! \n'
    'Расскажешь мне о залупе лягушки?'.format(bot.message.chat.first_name), reply_markup=my_keyboard)
    print(bot.message)

def get_anecdote(bot, update):
    receive = requests.get('http://anekdotme.ru/random')
    page = BeautifulSoup(receive.text, "html.parser")
    find = page.select('.anekdot_text')
    for text in find:
        page =(text.getText().strip())
    bot.message.reply_text(page)

def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)

def main():
    my_bot = Updater(TG_TOKEN, TG_API_URL, use_context=True)
    my_bot.dispatcher.add_handler(CommandHandler('start', sms))

    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Начать'), sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Анекдот'), get_anecdote))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))
    my_bot.start_polling()
    my_bot.idle()

main()


