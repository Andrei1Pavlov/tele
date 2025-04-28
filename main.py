from telebot import *
import json
from telebot.types import WebAppInfo

bot = telebot.TeleBot('7678063633:AAEr49462oXdZdwfR7pHABKre99KpxYJ_PM')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://andrei1pavlov.github.io/tele2/')))
    bot.send_message(message.chat.id,"Привет, мой друг", reply_markup=markup)


@bot.message_handler(content_types=['web_app_data'])
def web_app(message):
    res = json.loads(message.web_app_data.data)
    bot.send_message(
        message.chat.id,
        f'Имя: {res.get("name", "не указано")}\nEmail: {res.get("email", "не указан")}\nТелефон: {res.get("phone", "не указан")}'
    )




bot.polling(none_stop=True)




