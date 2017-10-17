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
setMessage('manager', 'tr', 'Biz de 9 ila 20, olmadan çıktı. E-posta @uzglobalkargo bizimle iletişim kurmak için.')


setMessage('what_i_can', 'ru', 'Отследить местонахождение вашего груза. Присылать уведомления о передвижении. Принять заказ на новую доставку.')
setMessage('what_i_can', 'tr', 'İzlemek için gönderinizin. E-posta bildirimleri ve hareket. Sipariş almak, yeni bir teslim.')


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

setMessage('m.0', 'tr', 'ocak')
setMessage('m.1', 'tr', 'şubat')
setMessage('m.2', 'tr', 'mart')
setMessage('m.3', 'tr', 'nisan')
setMessage('m.4', 'tr', 'mayıs')
setMessage('m.5', 'tr', 'haziran')
setMessage('m.6', 'tr', 'temmuz')
setMessage('m.7', 'tr', 'ağustos')
setMessage('m.8', 'tr', 'eylül')
setMessage('m.9', 'tr', 'ekim')
setMessage('m.10', 'tr', 'kasım')
setMessage('m.11', 'tr', 'aralık')

#Инфо о грузе
setMessage('i.your_track', 'ru', 'Ваш заказ,')
setMessage('i.contacts', 'ru', 'Контактные данные')
setMessage('i.cost', 'ru', 'Цена: ')
setMessage('i.weight', 'ru', 'Вес груза: ')
setMessage('i.note', 'ru', 'Примечание: ')
setMessage('i.tarif', 'ru', 'Тариф "Экспресс", ')
setMessage('i.days', 'ru', ' дня.')
setMessage('i.wait', 'ru', 'Ожидается доставка к ')
setMessage('i.price', 'ru', 'Ожидается оплата: ')
setMessage('i.pricey', 'ru', 'Произведена оплата в размере ')
setMessage('i.office', 'ru', 'Принято в головном офисе.')
setMessage('i.terr', 'ru', 'Прибыло на территорию Узбекистана')
setMessage('i.stambul', 'ru', 'Стамбул')
setMessage('i.tashkent', 'ru', 'Ташкент')

setMessage('i.your_track', 'tr', 'Siparişiniz,')
setMessage('i.contacts', 'tr', 'Iletişim detayları')
setMessage('i.cost', 'tr', 'Fiyat: ')
setMessage('i.weight', 'tr', 'Kargo ağırlığı: ')
setMessage('i.note', 'ru', 'Düşünce: ')
setMessage('i.tarif', 'tr', 'Tarife "Express", ')
setMessage('i.days', 'tr', ' gün.')
setMessage('i.wait', 'tr', 'Bekleniyor teslimat ')
setMessage('i.price', 'tr', 'Ödeme bekleniyor: ')
setMessage('i.pricey', 'tr', 'Ödeme miktarı ')
setMessage('i.office', 'tr', 'Anlaşıldı merkez ofisi.')
setMessage('i.terr', 'tr', 'Geldi toprakları, Özbekistan')
setMessage('i.stambul', 'tr', 'İstanbul')
setMessage('i.tashkent', 'tr', 'Taşkent')

#Новый заказ
setMessage("n.pre", "ru", "Для того чтобы сделать заказ.")
setMessage("n.name", "ru", "Ваше имя и фамилия.\n__Например, Мурат Демирджи__")
setMessage("n.phone", "ru", "Ваш номер телефона.\n_Например, 89001002030_")
setMessage("n.weight", "ru", "Укажите вес вашего груза без добавочных.\n_Например, 100_")
setMessage("n.address", "ru", "Укажите адрес доставки или город.\n_Например, Ташкент_")
setMessage("n.payed", "ru", "Выберите способ оплаты\n_Вы можете оплатить картой или наличными при получении в Узбекистане_\n_При оплате в офисе в Турции вы можете оплатить только наличными_")
setMessage("n.note", "ru", "Есть какие-либо дополнительные пожелания?")
setMessage("n.your_order", "ru", "Ваш заказ")
setMessage("n.result", "ru", "Итоговая сумма: $")
setMessage("n.tarif", "ru", "Тариф “Экспресс”, ")
setMessage("n.days", "ru", " дня, $")
setMessage("n.kg", "ru", "/кг")
setMessage("n.kgs", "ru", "кг")
setMessage("n.p1", "ru", "Оплата в Узбекистане")
setMessage("n.p2", "ru", "Оплата в офисе в Турции")
setMessage("n.order_yes", "ru", "Ваш заказ принят. Менеджер свяжется с вами в ближайшее время.")
setMessage("n.order_no", "ru", "Возврат к главному меню.")

setMessage("n.pre", "tr", "Yapmak için sipariş.")
setMessage("n.name", "tr", "Adı ve soyadı.")
setMessage("n.phone", "tr", "Telefon numarası")
setMessage("n.weight", "tr", "Ağırlığı belirtin kargo")
setMessage("n.address", "tr", "Adresi teslim")
setMessage("n.payed", "tr", "Bir ödeme yöntemi seçin")
setMessage("n.note", "tr", "Herhangi bir ek özellik istekleri?")
setMessage("n.your_order", "tr", "Sipariş")
setMessage("n.result", "tr", "Toplam: $")
setMessage("n.tarif", "tr", "Tarife ''Express'', ")
setMessage("n.days", "tr", " gün, $")
setMessage("n.kg", "tr", "/kg")
setMessage("n.kgs", "tr", "kg")
setMessage("n.p1", "tr", "Ödeme Özbekistan'da")
setMessage("n.p2", "tr", "Ödeme ofis Türkiye'de")
setMessage("n.order_yes", "tr", "Sipariş kabul edilir. Yöneticisi sizinle iletişime geçecektir yakında.")
setMessage("n.order_no", "tr", "Geri ana menü.")