import config, db
import telebot
from StateCore import *
import time, threading, requests

bot = telebot.TeleBot(config.token)

#bot.send_message(chatid, 'Чтобы продолжить, вам необходимо дать согласие на обработку и передачу своих персональных данных. Данные не будут переданы третьим лицам и сторонним организациям', reply_markup=keyboards.accept)
#bot.send_message(chatid, 'Введите /start, чтобы начать', reply_markup=keyboards.zero)
#bot.send_message(chatid, 'Здравствуйте, с помощью данного бота можно подать заявление на проживание в Турции через сайт https://e-ikamet.goc.gov.tr', reply_markup=keyboards.zero)
#bot.send_message(chatid, 'Напишите "Далее" для продолжения', reply_markup=keyboards.next)

@bot.callback_query_handler(func=lambda c: True)
def selectHandler(c):
    chatid = c.message.chat.id
    state = db.getState(chatid)
    if state == None:
        return
    state.handleSelect(c.data, chatid)

@bot.message_handler(commands=['start'])
def handle_start(message):
    chatid = message.chat.id
    state = db.getState(chatid)
    if state == None:
        state = StateStart()
        db.setState(chatid, state)
    state.handleStart(chatid)

@bot.message_handler(content_types=["text"])
def handler(message):
    chatid = message.chat.id
    if message.text == '':
        bot.send_message(chatid, 'Пожалуйста, введите текст..')
        return
    state = db.getState(chatid)
    if state == None:
        bot.send_message(chatid, 'Для начала работы введите /start')
        return
    state.handleMessage(chatid, message.text)

def eventsCheck():
    evr = requests.post('http://127.0.0.1/ajax/ajaxCore.php', data={'m': 'common', 'f': 'get_events'})
    print(evr)
    j = json.loads(evr)
    events = json.loads(j.msg)
    for event in events:
        chatid = int(event['chatid'])
        product_id = str(event['product_id'])
        sendTrackState(chatid, product_id)
    threading.Timer(10.0, eventsCheck).start()

if __name__ == '__main__':
    print('Бот успешно загружен')
    # bot.polling(none_stop=True)
    threading.Timer(10.0, eventsCheck).start()
    while True:
        try:
            bot.polling(none_stop=True)

        except Exception as e:
            print(e)
            time.sleep(15)
