from telebot import types

#Нулевая клавиатура
zero = types.ReplyKeyboardRemove()

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

class Locale:

    def __init__(self):
        self.ru = {}
        self.tr = {}

    def setKeyboard(self, name, lang, keyboard):
        if lang == 'ru':
            self.ru[name] = keyboard
        elif lang == 'tr':
            self.tr[name] = keyboard

    def getKeyboard(self, name, lang):
        if lang == 'ru':
            return self.ru[name]
        elif lang == 'tr':
            return self.tr[name]
        else:
            return None

loc = Locale()

tmp = types.InlineKeyboardMarkup()
tmp.add(types.InlineKeyboardButton(text='Отслеживание груза', callback_data='track'))
tmp.add(types.InlineKeyboardButton(text='Сделать заказ', callback_data='order'))
tmp.add(types.InlineKeyboardButton(text='Что я могу', callback_data='info'))
tmp.add(types.InlineKeyboardButton(text='Позвать менеджера', callback_data='manager'))
loc.setKeyboard('menu', 'ru', tmp)

tmp = types.InlineKeyboardMarkup()
tmp.add(types.InlineKeyboardButton(text='Yüklerin takibi', callback_data='track'))
tmp.add(types.InlineKeyboardButton(text='Sipariş ver', callback_data='order'))
tmp.add(types.InlineKeyboardButton(text='Ne yapabilirim?', callback_data='info'))
tmp.add(types.InlineKeyboardButton(text='Iletişim', callback_data='manager'))
loc.setKeyboard('menu', 'tr', tmp)

tmp = types.InlineKeyboardMarkup()
tmp.add(types.InlineKeyboardButton(text='Оплата в Узбекистане', callback_data='n.1'))
tmp.add(types.InlineKeyboardButton(text='Оплата в офисе в Турции', callback_data='n.2'))
loc.setKeyboard('payed', 'ru', tmp)

tmp = types.InlineKeyboardMarkup()
tmp.add(types.InlineKeyboardButton(text="Ödeme Özbekistan'da", callback_data='n.1'))
tmp.add(types.InlineKeyboardButton(text="Ödeme ofis Türkiye'de", callback_data='n.2'))
loc.setKeyboard('payed', 'tr', tmp)

tmp = types.InlineKeyboardMarkup()
tmp.add(types.InlineKeyboardButton(text='[Подтвердить]', callback_data='yes'))
tmp.add(types.InlineKeyboardButton(text='[Отмена]', callback_data='no'))
loc.setKeyboard('new_order_accept', 'ru', tmp)

tmp = types.InlineKeyboardMarkup()
tmp.add(types.InlineKeyboardButton(text='[Onaylamak]', callback_data='yes'))
tmp.add(types.InlineKeyboardButton(text='[İptal]', callback_data='no'))
loc.setKeyboard('new_order_accept', 'tr', tmp)

#Клавиатура для меню
# menu = types.ReplyKeyboardMarkup(True, False)
#menu = types.InlineKeyboardMarkup()
#menu.add(types.InlineKeyboardButton(text='Отслеживание груза',callback_data='track'))
#menu.add(types.InlineKeyboardButton(text='Сделать заказ',callback_data='order'))
#menu.add(types.InlineKeyboardButton(text='Информация',callback_data='info'))
#menu.add(types.InlineKeyboardButton(text='Позвать менеджера',callback_data='manager'))
#menu.row('Отслеживание груза')
#menu.row('Сделать заказ')
#menu.row('Информация')
#menu.row('Позвать менеджера')
#
# track = types.KeyboardButton('Отслеживание груза')
# menu.add(track)