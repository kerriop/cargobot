import telebot
from bot_core import *
import time
import config


@bot.callback_query_handler(func=lambda c: True)
def select_handler(c):
    chatid = c.message.chat.id
    state = db.get_state(chatid)
    if state is None:
        return
    state.handle_select(c.data, chatid)


@bot.message_handler(commands=['start'])
def handle_start(message):
    chatid = message.chat.id
    state = StateStart()
    db.set_state(chatid, state)
    state.handle_start(chatid)


@bot.message_handler(content_types=["text"])
def handler(message):
    chatid = message.chat.id
    if message.text == '':
        bot.send_message(chatid, 'Пожалуйста, введите текст..')
        return
    state = db.get_state(chatid)
    if state is None:
        bot.send_message(chatid, 'Для начала работы введите /start')
        return
    state.handle_message(chatid, message.text)


if __name__ == '__main__':
    bot = telebot.TeleBot(config.token)
    while True:
        try:
            print('Бот успешно загружен')
            bot.polling(none_stop=True)

        except Exception as e:
            print(e)
            time.sleep(15)
