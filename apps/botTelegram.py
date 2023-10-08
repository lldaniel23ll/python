import telebot

bot = telebot.TeleBot('5853035867:AAFf5aNIMaYEhCSA94LwbuFwbEMR810edZk')
@bot.message_handler(commands=['help','start'])

def send(message):
    bot.reply_to(message, 'que nota prix!')

bot.polling()
