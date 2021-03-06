from telebot import types

# Нулевая клавиатура
zero = types.ReplyKeyboardRemove()

# Клавиатура для этапа проверки данных
check_data = types.InlineKeyboardMarkup()
check_data.add(types.InlineKeyboardButton(text='Продолжить', callback_data='cd:ok'))
check_data.add(types.InlineKeyboardButton(text='Изменить поле', callback_data='cd:no'))

# Клавиатура для выбора языка
language = types.InlineKeyboardMarkup()
language.add(types.InlineKeyboardButton(text='Русский', callback_data='ru'))
language.add(types.InlineKeyboardButton(text='Türkçe', callback_data='tr'))

# Клавиатура далее
next = types.ReplyKeyboardMarkup(True, False)
next.row('Далее')

# Клавиатура согласия
accept = types.ReplyKeyboardMarkup(True, False)
accept.row('Даю согласие', 'Не даю согласие')


class Locale:

    def __init__(self):
        self.ru = {}
        self.tr = {}

    def set_keyboard(self, name, lang, keyboard):
        if lang == 'ru':
            self.ru[name] = keyboard
        elif lang == 'tr':
            self.tr[name] = keyboard

    def get_keyboard(self, name, lang):
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
loc.set_keyboard('menu', 'ru', tmp)

tmp = types.InlineKeyboardMarkup()
tmp.add(types.InlineKeyboardButton(text='Yüklerin takibi', callback_data='track'))
tmp.add(types.InlineKeyboardButton(text='Sipariş ver', callback_data='order'))
tmp.add(types.InlineKeyboardButton(text='Ne yapabilirim?', callback_data='info'))
tmp.add(types.InlineKeyboardButton(text='Iletişim', callback_data='manager'))
loc.set_keyboard('menu', 'tr', tmp)

tmp = types.InlineKeyboardMarkup()
tmp.add(types.InlineKeyboardButton(text='Оплата в Узбекистане', callback_data='n.1'))
tmp.add(types.InlineKeyboardButton(text='Оплата в офисе в Турции', callback_data='n.2'))
loc.set_keyboard('payed', 'ru', tmp)

tmp = types.InlineKeyboardMarkup()
tmp.add(types.InlineKeyboardButton(text="Ödeme Özbekistan'da", callback_data='n.1'))
tmp.add(types.InlineKeyboardButton(text="Ödeme ofis Türkiye'de", callback_data='n.2'))
loc.set_keyboard('payed', 'tr', tmp)

tmp = types.InlineKeyboardMarkup()
tmp.add(types.InlineKeyboardButton(text='[Подтвердить]', callback_data='yes'))
tmp.add(types.InlineKeyboardButton(text='[Отмена]', callback_data='no'))
loc.set_keyboard('new_order_accept', 'ru', tmp)

tmp = types.InlineKeyboardMarkup()
tmp.add(types.InlineKeyboardButton(text='[Onaylamak]', callback_data='yes'))
tmp.add(types.InlineKeyboardButton(text='[İptal]', callback_data='no'))
loc.set_keyboard('new_order_accept', 'tr', tmp)