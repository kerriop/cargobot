import telebot
from telebot import types

another_token = "405566328:AAE7ACc8_ucVEL_qAic8wcrkQae_Y-8kcW0"
lang = "ru"
start_msg = "Привет, я бот Uzglobalkargo." \
            " Я могу отследить ваш груз по вашему трэк-коду, " \
            "присылать уведомления о доставке груза." \
            " Еще могу принимать новые заказы на отправку грузов из Турции в Узбекистан."

# menu
info_menu = "Что я могу"
order_menu = "Сделать заказ"
search_menu = "Отслеживание груза"
manager_menu = "Связаться с менеджером"


bot = telebot.TeleBot(another_token)

# @bot.message_handler(commands=['start'])
# def start(message):
#     sent = bot.send_message(message.chat.id, 'ТЫ КТО!?')
#     bot.register_next_step_handler(sent, hello)
#
# def hello(message):
#     bot.send_message(
#         message.chat.id,
#         'Привет, {name}. Рад тебя видеть.'.format(name=message.text))

@bot.message_handler(commands=["start"])
def request_contact(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
    button_contact = types.KeyboardButton(text="start",request_contact=True)
    keyboard.add(button_contact)
    msg = bot.send_message(message.chat.id, start_msg)
    bot.register_next_step_handler(msg, start)

def start(message):
    #Переводы
    if lang == "ru":
        # start_msg
        info_menu = "Что я могу"
        order_menu = "Сделать заказ"
        search_menu = "Отслеживание груза"
        manager_menu = "Связаться с менеджером"
    elif lang == "tr":
        # start_msg = "*говорит по-турецки*"
        info_menu = "*говорит по-турецки*"
        order_menu = "*говорит по-турецки*"
        search_menu = "*говорит по-турецки*"
        manager_menu = "*говорит по-турецки*"

    # Главное меню
    start_markup = types.ReplyKeyboardMarkup(True, False)
    start_markup.row('Turkey', 'Русский язык')
    start_markup.row(' ' + info_menu + ' ')
    start_markup.row(' ' + order_menu + ' ')
    start_markup.row(' ' + search_menu + ' ')
    start_markup.row(' ' + manager_menu + ' ')
    bot.send_message(message.chat.id, reply_markup=start_markup)


@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == 'Русский язык':
        lang = 'ru'
        msg = bot.send_message(message.chat.id, 'Вы выбрали русский язык -' + lang + '-')
        bot.register_next_step_handler(msg, start)

    elif message.text == info_menu:
        msg = bot.send_message(message.chat.id, "*Отследить местонахождение вашего груза*\n"
                                                "*Присылать уведомления о передвижении*\n"
                                                "*Принять заказ на новую доставку*\n")
        bot.register_next_step_handler(msg, start)
    #
    # elif message.text == order_menu:
    #     msg = bot.send_message(message.chat.id, "*Что-то про заказы*")
    #     bot.register_next_step_handler(msg, start)
    #
    # elif message.text == search_menu:
    #     msg = bot.send_message(message.chat.id, "*Что-то про грузы*")
    #     bot.register_next_step_handler(msg, start)
    #
    # elif message.text == manager_menu:
    #     msg = bot.send_message(message.chat.id, "*Что-то про манагера*")
    #     bot.register_next_step_handler(msg, start)



bot.polling(none_stop=True)