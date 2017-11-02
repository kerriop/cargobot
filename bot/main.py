import telebot
from StateCore import *
import time

bot = telebot.TeleBot(config.token)

#bot.send_message(chatid, 'Чтобы продолжить, вам необходимо дать согласие на обработку и передачу своих персональных данных. Данные не будут переданы третьим лицам и сторонним организациям', reply_markup=keyboards.accept)
#bot.send_message(chatid, 'Введите /start, чтобы начать', reply_markup=keyboards.zero)
#bot.send_message(chatid, 'Здравствуйте, с помощью данного бота можно подать заявление на проживание в Турции через сайт https://e-ikamet.goc.gov.tr', reply_markup=keyboards.zero)
#bot.send_message(chatid, 'Напишите "Далее" для продолжения', reply_markup=keyboards.next)


@bot.callback_query_handler(func=lambda c: True)
def select_handler(c):
    chatid = c.message.chat.id
    state = db.getState(chatid)
    if state is not None:
        return
    state.handle_select(c.data, chatid)


@bot.message_handler(commands=['start'])
def handle_start(message):
    chatid = message.chat.id
    state = StateStart()
    db.setState(chatid, state)
    state.handle_start(chatid)


@bot.message_handler(content_types=["text"])
def handler(message):
    chatid = message.chat.id
    if message.text == '':
        bot.send_message(chatid, 'Пожалуйста, введите текст..')
        return
    state = db.getState(chatid)
    if state is None:
        bot.send_message(chatid, 'Для начала работы введите /start')
        return
    state.handle_message(chatid, message.text)


if __name__ == '__main__':
    while True:
        try:
            print('Бот успешно загружен')
            bot.polling(none_stop=True)

        except Exception as e:
            print(e)
            time.sleep(15)
