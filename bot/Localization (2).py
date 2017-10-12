ru = {}
tr = {}

def setMessage(name, lang, message):
    if lang == 'ru':
        ru[name] = message
    elif lang == 'tr':
        tr[name] = message

def getMessage(name, lang):
    if lang == 'ru':
        message = ru[name]
    elif lang == 'tr':
        message = tr[name]

    if message is not None:
        return str(message)
    else:
        return ''


setMessage('select_action', 'ru', 'Выберите действие: ')
setMessage('select_action', 'tr', 'Bir eylem seçin: ')

setMessage('enter_client_code', 'ru', 'Введите ваш клиентский номер: ')
setMessage('enter_client_code', 'tr', 'Yazın hesap numarasını: ')

setMessage('manager', 'ru', 'Мы работаем с 9 до 20, без выходных. Напишите на @uzglobalkargo для связи с нами.')


setMessage('what_i_can', 'ru', 'Отследить местонахождение вашего груза. Присылать уведомления о передвижении. Принять заказ на новую доставку')


#Месяцы
setMessage('m.0', 'ru', 'янв')
setMessage('m.1', 'ru', 'фев')
setMessage('m.2', 'ru', 'мар')
setMessage('m.3', 'ru', 'апр')
setMessage('m.4', 'ru', 'май')
setMessage('m.5', 'ru', 'июн')
setMessage('m.6', 'ru', 'июл')
setMessage('m.7', 'ru', 'авг')
setMessage('m.8', 'ru', 'сен')
setMessage('m.9', 'ru', 'окт')
setMessage('m.10', 'ru', 'ноя')
setMessage('m.11', 'ru', 'дек')

#Инфо о грузе
setMessage('i.your_track', 'ru', 'Ваша посылка, ')
setMessage('i.tarif', 'ru', 'Тариф "Экспресс", ')
setMessage('i.days', 'ru', ' дня.')
setMessage('i.wait', 'ru', 'Ожидается доставка к ')
setMessage('i.price', 'ru', 'Ожидается оплата: ')
setMessage('i.pricey', 'ru', 'Произведена оплата в размере ')
setMessage('i.office', 'ru', 'Принято в головном офисе.')
setMessage('i.terr', 'ru', 'Прибыло на территорию Узбекистана')
setMessage('i.stambul', 'ru', 'Стамбул')
setMessage('i.tashkent', 'ru', 'Ташкент')

#Новый заказ
setMessage('n.pre', 'ru', 'Для того чтобы сделать заказ.')
setMessage('n.name', 'ru', 'Ваше имя и фамилия.')
setMessage('n.phone', 'ru', 'Ваш номер телефона')
setMessage('n.weight', 'ru', 'Укажите вес вашего груза')
setMessage('n.address', 'ru', 'Укажите адрес доставки')
setMessage('n.payed', 'ru', 'Выберите способ оплаты')
setMessage('n.note', 'ru', 'Есть какие-либо дополнительные пожелания?')
setMessage('n.your_order', 'ru', 'Ваш заказ')
setMessage('n.result', 'ru', 'Итоговая сумма: $')
setMessage('n.tarif', 'ru', 'Тариф “Экспресс”, ')
setMessage('n.days', 'ru', ' дня, $')
setMessage('n.kg', 'ru', '/кг')