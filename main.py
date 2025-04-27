import telebot
from telebot import *

from telebot.types import WebAppInfo

bot = telebot.TeleBot('7678063633:AAEr49462oXdZdwfR7pHABKre99KpxYJ_PM')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://andrei1pavlov.github.io/tele/')))
    bot.send_message(message.chat.id,"Привет, мой друг", reply_markup=markup)



bot.polling(none_stop=True)




