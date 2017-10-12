from telebot import types
import re
import requests
import time

#Нулевая клавиатура
zero = types.ReplyKeyboardRemove()

#Клавиатура с командой /start
start = types.ReplyKeyboardMarkup()
start.row('/start')

#Клавиатура выбора пола
sex = types.ReplyKeyboardMarkup(True, False)
sex.row('М', 'Ж')

#Клавиатура для этапа проверки данных
checkData = types.InlineKeyboardMarkup()
checkData.add(types.InlineKeyboardButton(text='Продолжить', callback_data='cd:ok'))
checkData.add(types.InlineKeyboardButton(text='Изменить поле', callback_data='cd:no'))

#Клавиатура для выбора языка
language = types.InlineKeyboardMarkup()
language.add(types.InlineKeyboardButton(text='Русский', callback_data='ru'))
language.add(types.InlineKeyboardButton(text='Türkçe', callback_data='tr'))

#Клавиатура далее
next = types.ReplyKeyboardMarkup(True, False)
next.row('Далее')

#Клавиатура согласия
accept = types.ReplyKeyboardMarkup(True, False)
accept.row('Даю согласие', 'Не даю согласие')

#Клавиатура для меню
menu = types.ReplyKeyboardMarkup(True, False)
# menu = types.InlineKeyboardMarkup()
# menu.add(types.InlineKeyboardButton(text='Отслеживание груза',callback_data='track'))
# menu.add(types.InlineKeyboardButton(text='Сделать заказ',callback_data='order'))
# menu.add(types.InlineKeyboardButton(text='Информация',callback_data='info'))
# menu.add(types.InlineKeyboardButton(text='Позвать менеджера',callback_data='manager'))
menu.row('Отслеживание груза')
menu.row('Сделать заказ')
menu.row('Информация')
menu.row('Позвать менеджера')
#
# track = types.KeyboardButton('Отслеживание груза')
# menu.add(track)