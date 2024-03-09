import os

from dotenv import load_dotenv
import telebot
from telebot import types

load_dotenv()
BOT_TOKEN = os.environ.get('TELEGRAM_API')
bot = telebot.TeleBot(BOT_TOKEN)

hello_msg = "Приветствую! \nЭто тестовый бот, через который можно посмотреть моё резюме, github и контакты."


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton('Резюме 🌐', callback_data='resume')
    btn2 = types.InlineKeyboardButton('Github 💻', callback_data='github')
    btn3 = types.InlineKeyboardButton('Контакты 👥 💬', callback_data='contacts')

    markup.add(btn1, btn2, btn3)

    bot.reply_to(message, hello_msg,
                 reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    if call.data == 'resume':
        bot.send_message(call.message.chat.id, 'Ссылка на резюме:\nhttp://45.138.163.236:54322/')

    elif call.data == 'github':
        bot.send_message(call.message.chat.id, 'Ссылка на гитхаб:\nhttps://github.com/Tim-Sa') 

    elif call.data == 'contacts':
        bot.send_message(call.message.chat.id, 'Почта:\nSalnikovtimofeyof@gmail.com\nТелефон: \n8 (968) 885-35-83') 

def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()