from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters


def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?')
    bot.message.reply_text('Здравствуйте, {}! \n'
    'Поговорите со мной!'.format(bot.message.chat.first_name))
    print(bot.message)

def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)

def main():
    my_bot = Updater("1352673032:AAEfDbWv6Up8U1Z2cGb9CbyCc7j9BG7zIpE","https://telegg.ru/orig/bot", use_context=True)

    my_bot.dispatcher.add_handler(CommandHandler('start',sms))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))
    my_bot.start_polling()
    my_bot.idle()

main()


