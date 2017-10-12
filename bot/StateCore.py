import db, main, keyboards, Localization
import requests, json

class StateCore:

    def __init__(self):
        pass

    def handleStart(self, chatid):
        pass

    def handleMessage(self, message, chatid):
        print('handleText: ' + str(message))

    def handleSelect(self, data, chatid):
        print('handleSelect: ' + str(data))

    def reset(self, chatid):
        pass



class StateStart(StateCore):

    def handleStart(self, chatid):
        state = StateWaitNext()
        db.setState(chatid, state)
        main.bot.send_message(chatid, "Привет, я бот Uzglobalkargo. Я могу отследить ваш груз по вашему трэк-коду, присылать уведомления о доставке груза. Еще могу принимать новые заказы на отправку грузов из Турции в Узбекистан. Для продолжения напишите 'Далее'", reply_markup=keyboards.next)



class StateWaitNext(StateCore):

    def handleMessage(self, chatid, message):
        if message == 'Далее':
            state = StateLicense()
            db.setState(chatid, state)
            main.bot.send_message(chatid, 'Чтобы продолжить, вам необходимо дать согласие на обработку и передачу своих персональных данных. Данные не будут переданы третьим лицам и сторонним организациям', reply_markup=keyboards.accept)


class StateLicense(StateCore):

    def handleMessage(self, chatid, message):
        if message == 'Даю согласие':
            state = StateLanguage()
            db.setState(chatid, state)
            main.bot.send_message(chatid, 'Выберите', reply_markup=keyboards.zero)
            main.bot.send_message(chatid, 'свой язык:', reply_markup=keyboards.language)

def returnToMainMenu(chatid):
    state = StateMenu()
    db.setState(chatid, state)
    state.reset(chatid)


class StateLanguage(StateCore):

    def handleSelect(self, data, chatid):
        code = str(data)
        if code == 'ru':
            db.setLang(chatid, 'ru')
        elif code == 'tr':
            db.setLang(chatid, 'tr')
        else:
            return
        returnToMainMenu(chatid)



class StateMenu(StateCore):

    def reset(self, chatid):
        code = db.getLang(chatid)
        main.bot.send_message(chatid, Localization.getMessage('select_action', code), reply_markup=keyboards.loc.getKeyboard('menu', code))

    def handleSelect(self, data, chatid):
        lang = db.getLang(chatid)
        code = str(data)
        if code == 'track':
            state = MenuTrackState()
            db.setState(chatid, state)
            main.bot.send_message(chatid, Localization.getMessage('enter_client_code', lang), reply_markup=keyboards.zero)
        elif code == 'order':
            state = MenuNewOrderState()
            db.setState(chatid, state)
            state.reset(chatid)
        elif code == 'info':
            main.bot.send_message(chatid, Localization.getMessage('what_i_can', lang), reply_markup=keyboards.zero)
            self.reset(chatid)
        elif code == 'manager':
            main.bot.send_message(chatid, Localization.getMessage('manager', lang), reply_markup=keyboards.zero)
            self.reset(chatid)


class MenuNewOrderState(StateCore):

    def __init__(self):
        self.substate = 0

    def reset(self, chatid):
        lang = db.getLang(chatid)
        main.bot.send_message(chatid, Localization.getMessage('n.pre', lang), reply_markup=keyboards.zero)
        main.bot.send_message(chatid, Localization.getMessage('n.name', lang), reply_markup=keyboards.zero)
        self.substate = 0

    def handleSelect(self, data, chatid):
        lang = db.getLang(chatid)
        data = str(data)
        if self.substate == 10:
            if data == 'yes':
                main.bot.send_message(chatid, Localization.getMessage('n.order_yes', lang), reply_markup=keyboards.zero)
                r = requests.post('http://sys.uzglobal.space/ajax/ajaxCore.php', data={
                    'm': 'common',
                    'f': 'add_product_bot',
                    'name': self.name,
                    'phone': self.phone,
                    'weight': self.weight,
                    'payed': self.payed,
                    'address': self.address,
                    'note': self.note
                });
                returnToMainMenu(chatid)
            elif data == 'no':
                main.bot.send_message(chatid, Localization.getMessage('n.order_no', lang), reply_markup=keyboards.zero)
                returnToMainMenu(chatid)
        else:
            if (data.startswith('n.')) and (self.substate == 4):
                self.payed = int(data[len('n.'):])
                self.substate = 5
                main.bot.send_message(chatid, Localization.getMessage('n.note', lang), reply_markup=keyboards.zero)
            else:
                return

    def sendOrderInfo(self, chatid, lang):
        r = requests.post('http://sys.uzglobal.space/ajax/ajaxCore.php', data={'m': 'common', 'f': 'common_info', 'weight': self.weight})
        j = json.loads(r.text)
        if j['err'] == '1':
            main.bot.send_message(chatid, 'Internal error!', reply_markup=keyboards.zero)
            returnToMainMenu(chatid)
            return
        j = json.loads(j['msg'])
        main.bot.send_message(chatid, Localization.getMessage('n.your_order', lang), reply_markup=keyboards.zero)
        main.bot.send_message(chatid, self.name + ',', reply_markup=keyboards.zero)
        main.bot.send_message(chatid, self.phone, reply_markup=keyboards.zero)
        main.bot.send_message(chatid, str(self.weight) + ' ' + Localization.getMessage('n.kgs', lang), reply_markup=keyboards.zero)
        main.bot.send_message(chatid, self.address, reply_markup=keyboards.zero)
        main.bot.send_message(chatid, Localization.getMessage('n.p' + str(self.payed), lang), reply_markup=keyboards.zero)
        main.bot.send_message(chatid, self.note, reply_markup=keyboards.zero)
        main.bot.send_message(chatid, Localization.getMessage('n.result', lang) + str(j['price']), reply_markup=keyboards.zero)
        main.bot.send_message(chatid, Localization.getMessage('n.tarif', lang) +
                              str(j['from']) + '-' + str(j['to']) +
                              Localization.getMessage('n.days', lang) +
                              str(j['selfCost']) +
                              Localization.getMessage('n.kg', lang), reply_markup=keyboards.loc.getKeyboard('new_order_accept', lang))

    def handleMessage(self, chatid, message):
        lang = db.getLang(chatid)
        if self.substate == 0:
            self.name = message
            self.substate = 1
            main.bot.send_message(chatid, Localization.getMessage('n.phone', lang), reply_markup=keyboards.zero)
        elif self.substate == 1:
            if not(message.isdigit()):
                main.bot.send_message(chatid, 'Wrong phone format! Only digits without spaces or symbols!', reply_markup=keyboards.zero)
                return
            self.phone = message
            self.substate = 2
            main.bot.send_message(chatid, Localization.getMessage('n.weight', lang), reply_markup=keyboards.zero)
        elif self.substate == 2:
            if not(message.isdigit()):
                main.bot.send_message(chatid, 'Wrong weight!', reply_markup=keyboards.zero)
                return
            self.weight = int(message)
            self.substate = 3
            main.bot.send_message(chatid, Localization.getMessage('n.address', lang), reply_markup=keyboards.zero)
        elif self.substate == 3:
            self.address = message
            self.substate = 4
            main.bot.send_message(chatid, Localization.getMessage('n.payed', lang), reply_markup=keyboards.loc.getKeyboard('payed', lang))
        elif self.substate == 5:
            self.note = message
            self.substate = 10
            self.sendOrderInfo(chatid, lang)


class MenuTrackState(StateCore):

    def handleMessage(self, chatid, message):
        lang = db.getLang(chatid)
        message = str(message)
        if message.startswith('TR-UZ-'):
            id = int(message[len('TR-UZ-'):])
            trackCode = str(message)
        else:
            if not(message.isdigit()):
                returnToMainMenu(chatid)
                return
            id = int(message)
            if (id >= 1000) or (id < 0):
                returnToMainMenu(chatid)
                return
            trackCode = 'TR-UZ-' + str(id).rjust(3, '0')

        r = requests.post('http://sys.uzglobal.space/ajax/ajaxCore.php', data={'m': 'common', 'f': 'product_info', 'id': id})
        j = json.loads(r.text)
        if j['err'] == '1':
            main.bot.send_message(chatid, 'Internal error!', reply_markup=keyboards.zero)
            returnToMainMenu(chatid)
            return
        j = json.loads(j['msg'])
        print(j)
        main.bot.send_message(chatid, Localization.getMessage('i.your_track', lang) + str(j['name']) + '. ' + trackCode, reply_markup=keyboards.zero)
        main.bot.send_message(chatid, Localization.getMessage('i.tarif', lang) + str(j['from']) + '-' + str(j['to']) + Localization.getMessage('i.days', lang), reply_markup=keyboards.zero)
        main.bot.send_message(chatid, Localization.getMessage('i.wait', lang) + str(j['day']) + ' ' + Localization.getMessage('m.' + str(j['month']), lang), reply_markup=keyboards.zero)
        if int(j['payed']) == 1:
            main.bot.send_message(chatid, Localization.getMessage('i.pricey', lang) + str(j['price']) + '$', reply_markup=keyboards.zero)
        else:
            main.bot.send_message(chatid, Localization.getMessage('i.price', lang) + str(j['price']) + '$', reply_markup=keyboards.zero)
        pstate = int(j['state'])
        if pstate == 0:
            #головной офис
            main.bot.send_message(chatid, Localization.getMessage('i.office', lang), reply_markup=keyboards.zero)
            main.bot.send_message(chatid, str(j['date']) + Localization.getMessage('i.stambul', lang), reply_markup=keyboards.zero)
        elif pstate >= 1:
            #терр.
            main.bot.send_message(chatid, Localization.getMessage('i.terr', lang), reply_markup=keyboards.zero)
            main.bot.send_message(chatid, str(j['date']) + Localization.getMessage('i.tashkent', lang), reply_markup=keyboards.zero)
        returnToMainMenu(chatid)