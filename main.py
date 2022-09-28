import config
import button
import telebot
import json


bot = telebot.TeleBot(config.Token)


with open('languages.json', 'r') as JSON:
    json.load(JSON)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет✌ я бот FisHelper, я показываю температура в водоъемах в Московской '
                                      'области, дальше используй кнопки!', reply_markup=button.welcome())


@bot.message_handler(content_types=['text'])
def about(message):
    if message.text == 'О нас':
        bot.send_message(message.chat.id, 'Выберите нужный раздел', reply_markup=button.about())

    if message.text == 'Языки':
        bot.send_message(message.chat.id, 'Выберите нужный язык', reply_markup=button.languages())

    if message.text == 'Температуры водоемов':
        pass


if __name__ == '__main__':
    bot.polling()