ru = {}
tr = {}

def set_message(name, lang, message):
    if lang == 'ru':
        ru[name] = message
    elif lang == 'tr':
        tr[name] = message

def get_message(name, lang):
    if lang == 'ru':
        message = ru[name]
    elif lang == 'tr':
        message = tr[name]

    if message is not None:
        return str(message)
    else:
        return ''


set_message('select_action', 'ru', 'Выберите действие: ')
set_message('select_action', 'tr', 'Bir eylem seçin: ')

set_message('enter_client_code', 'ru', 'Введите ваш клиентский номер: ')
set_message('enter_client_code', 'tr', 'Yazın hesap numarasını: ')

set_message('manager', 'ru', 'Мы работаем с 9 до 20, без выходных. Напишите на @uzglobalkargo для связи с нами.')
set_message('manager', 'tr', 'Biz de 9 ila 20, olmadan çıktı. E-posta @uzglobalkargo bizimle iletişim kurmak için.')

set_message('what_i_can', 'ru',
            'Отследить местонахождение вашего груза. Присылать уведомления о передвижении. Принять заказ на новую '
            'доставку.')
set_message('what_i_can', 'tr',
            'İzlemek için gönderinizin. E-posta bildirimleri ve hareket. Sipariş almak, yeni bir teslim.')


#Месяцы
set_message('m.0', 'ru', 'янв')
set_message('m.1', 'ru', 'фев')
set_message('m.2', 'ru', 'мар')
set_message('m.3', 'ru', 'апр')
set_message('m.4', 'ru', 'май')
set_message('m.5', 'ru', 'июн')
set_message('m.6', 'ru', 'июл')
set_message('m.7', 'ru', 'авг')
set_message('m.8', 'ru', 'сен')
set_message('m.9', 'ru', 'окт')
set_message('m.10', 'ru', 'ноя')
set_message('m.11', 'ru', 'дек')

set_message('m.0', 'tr', 'ocak')
set_message('m.1', 'tr', 'şubat')
set_message('m.2', 'tr', 'mart')
set_message('m.3', 'tr', 'nisan')
set_message('m.4', 'tr', 'mayıs')
set_message('m.5', 'tr', 'haziran')
set_message('m.6', 'tr', 'temmuz')
set_message('m.7', 'tr', 'ağustos')
set_message('m.8', 'tr', 'eylül')
set_message('m.9', 'tr', 'ekim')
set_message('m.10', 'tr', 'kasım')
set_message('m.11', 'tr', 'aralık')

#Инфо о грузе
set_message('i.your_track', 'ru', 'Ваш заказ,')
set_message('i.contacts', 'ru', 'Контактные данные')
set_message('i.cost', 'ru', 'Цена: ')
set_message('i.weight', 'ru', 'Вес груза: ')
set_message('i.note', 'ru', 'Примечание: ')
set_message('i.tarif', 'ru', 'Тариф "Экспресс", ')
set_message('i.days', 'ru', ' дня.')
set_message('i.wait', 'ru', 'Ожидается доставка к ')
set_message('i.price', 'ru', 'Ожидается оплата: ')
set_message('i.pricey', 'ru', 'Произведена оплата в размере ')
set_message('i.office', 'ru', 'Принято в головном офисе.')
set_message('i.terr', 'ru', 'Прибыло на территорию Узбекистана')
set_message('i.stambul', 'ru', 'Стамбул')
set_message('i.tashkent', 'ru', 'Ташкент')

set_message('i.your_track', 'tr', 'Siparişiniz,')
set_message('i.contacts', 'tr', 'Iletişim detayları')
set_message('i.cost', 'tr', 'Fiyat: ')
set_message('i.weight', 'tr', 'Kargo ağırlığı: ')
set_message('i.note', 'ru', 'Düşünce: ')
set_message('i.tarif', 'tr', 'Tarife "Express", ')
set_message('i.days', 'tr', ' gün.')
set_message('i.wait', 'tr', 'Bekleniyor teslimat ')
set_message('i.price', 'tr', 'Ödeme bekleniyor: ')
set_message('i.pricey', 'tr', 'Ödeme miktarı ')
set_message('i.office', 'tr', 'Anlaşıldı merkez ofisi.')
set_message('i.terr', 'tr', 'Geldi toprakları, Özbekistan')
set_message('i.stambul', 'tr', 'İstanbul')
set_message('i.tashkent', 'tr', 'Taşkent')

#Новый заказ
set_message("n.pre", "ru", "Для того чтобы сделать заказ.")
set_message("n.name", "ru", "Ваше имя и фамилия.\n_Например, Мурат Демирджи_")
set_message("n.phone", "ru", "Ваш номер телефона.\n_Например, 89001002030_")
set_message("n.weight", "ru", "Укажите вес вашего груза без добавочных.\n_Например, 100_")
set_message("n.address", "ru", "Укажите адрес доставки или город.\n_Например, Ташкент_")
set_message("n.payed", "ru",
            "Выберите способ оплаты\n_Вы можете оплатить картой или наличными при получении в Узбекистане_\n_При "
            "оплате в офисе в Турции вы можете оплатить только наличными_")
set_message("n.note", "ru", "Есть какие-либо дополнительные пожелания?")
set_message("n.your_order", "ru", "Ваш заказ")
set_message("n.result", "ru", "Итоговая сумма: $")
set_message("n.tarif", "ru", "Тариф “Экспресс”, ")
set_message("n.days", "ru", " дня, $")
set_message("n.kg", "ru", "/кг")
set_message("n.kgs", "ru", "кг")
set_message("n.p1", "ru", "Оплата в Узбекистане")
set_message("n.p2", "ru", "Оплата в офисе в Турции")
set_message("n.order_yes", "ru", "Ваш заказ принят. Менеджер свяжется с вами в ближайшее время.")
set_message("n.order_no", "ru", "Возврат к главному меню.")

set_message("n.pre", "tr", "Yapmak için sipariş.")
set_message("n.name", "tr", "Adı ve soyadı.")
set_message("n.phone", "tr", "Telefon numarası")
set_message("n.weight", "tr", "Ağırlığı belirtin kargo")
set_message("n.address", "tr", "Adresi teslim")
set_message("n.payed", "tr", "Bir ödeme yöntemi seçin")
set_message("n.note", "tr", "Herhangi bir ek özellik istekleri?")
set_message("n.your_order", "tr", "Sipariş")
set_message("n.result", "tr", "Toplam: $")
set_message("n.tarif", "tr", "Tarife ''Express'', ")
set_message("n.days", "tr", " gün, $")
set_message("n.kg", "tr", "/kg")
set_message("n.kgs", "tr", "kg")
set_message("n.p1", "tr", "Ödeme Özbekistan'da")
set_message("n.p2", "tr", "Ödeme ofis Türkiye'de")
set_message("n.order_yes", "tr", "Sipariş kabul edilir. Yöneticisi sizinle iletişime geçecektir yakında.")
set_message("n.order_no", "tr", "Geri ana menü.")