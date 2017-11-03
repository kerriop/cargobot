import db
import main
import keyboards
import localization
import requests
import json
import config


class StateCore:

    def __init__(self):
        pass

    def handle_start(self, chatid):
        pass

    def handle_message(self, message, chatid):
        print('handleText: ' + str(message))

    def handle_select(self, data, chatid):
        print('handleSelect: ' + str(data))

    def reset(self, chatid):
        pass


class StateStart(StateCore):

    def handle_start(self, chatid):
        state = StateWaitNext()
        db.set_state(chatid, state)
        main.bot.send_message(chatid, "Привет, я бот Uzglobalkargo. Я могу отследить ваш груз по вашему трэк-коду, "
                                      "присылать уведомления о доставке груза. Еще могу принимать новые заказы на "
                                      "отправку грузов из Турции в Узбекистан. Для продолжения напишите 'Далее'",
                              reply_markup=keyboards.next)


class StateWaitNext(StateCore):

    def handle_message(self, chatid, message):
        if message == 'Далее':
            state = StateLicense()
            db.set_state(chatid, state)
            main.bot.send_message(chatid, 'Чтобы продолжить, вам необходимо дать согласие на обработку и передачу '
                                          'своих персональных данных. Данные не будут переданы третьим лицам и '
                                          'сторонним организациям',
                                  reply_markup=keyboards.accept)


class StateLicense(StateCore):

    def handle_message(self, chatid, message):
        if message == 'Даю согласие':
            state = StateLanguage()
            db.set_state(chatid, state)
            main.bot.send_message(chatid, 'Выберите', reply_markup=keyboards.zero)
            main.bot.send_message(chatid, 'свой язык:', reply_markup=keyboards.language)


def return_to_main_menu(chatid):
    state = StateMenu()
    db.set_state(chatid, state)
    state.reset(chatid)


class StateLanguage(StateCore):

    def handle_select(self, data, chatid):
        code = str(data)
        if code == 'ru':
            db.set_lang(chatid, 'ru')
        elif code == 'tr':
            db.set_lang(chatid, 'tr')
        else:
            return
        return_to_main_menu(chatid)


class StateMenu(StateCore):

    def reset(self, chatid):
        code = db.get_lang(chatid)
        main.bot.send_message(chatid, localization.get_message('select_action', code),
                              reply_markup=keyboards.loc.get_keyboard('menu', code))

    def handle_select(self, data, chatid):
        lang = db.get_lang(chatid)
        code = str(data)
        if code == 'track':
            state = MenuTrackState()
            db.set_state(chatid, state)
            main.bot.send_message(chatid, localization.get_message('enter_client_code', lang),
                                  reply_markup=keyboards.zero)
        elif code == 'order':
            state = MenuNewOrderState()
            db.set_state(chatid, state)
            state.reset(chatid)
        elif code == 'info':
            main.bot.send_message(chatid, localization.get_message('what_i_can', lang), reply_markup=keyboards.zero)
            self.reset(chatid)
        elif code == 'manager':
            main.bot.send_message(chatid, localization.get_message('manager', lang), reply_markup=keyboards.zero)
            self.reset(chatid)

    def handle_message(self, message, chatid):
        self.reset(chatid)


class MenuNewOrderState(StateCore):

    def __init__(self):
        self.substate = 0

    def reset(self, chatid):
        lang = db.get_lang(chatid)
        main.bot.send_message(chatid, localization.get_message('n.pre', lang), reply_markup=keyboards.zero,
                              parse_mode='markdown')
        main.bot.send_message(chatid, localization.get_message('n.name', lang), reply_markup=keyboards.zero,
                              parse_mode='markdown')
        self.substate = 0

    def handle_select(self, data, chatid):
        lang = db.get_lang(chatid)
        data = str(data)
        if self.substate == 10:
            if data == 'yes':
                main.bot.send_message(chatid, localization.get_message('n.order_yes', lang), reply_markup=keyboards.zero,
                                      parse_mode='markdown')
                r = requests.post(config.site_base + 'ajax/ajaxCore.php', data={
                    'm': 'common',
                    'f': 'add_product_bot',
                    'name': self.name,
                    'phone': self.phone,
                    'weight': self.weight,
                    'payed': self.payed,
                    'address': self.address,
                    'note': self.note
                });
                return_to_main_menu(chatid)
            elif data == 'no':
                main.bot.send_message(chatid, localization.get_message('n.order_no', lang), reply_markup=keyboards.zero,
                                      parse_mode='markdown')
                return_to_main_menu(chatid)
        else:
            if (data.startswith('n.')) and (self.substate == 4):
                self.payed = int(data[len('n.'):])
                self.substate = 5
                main.bot.send_message(chatid, localization.get_message('n.note', lang), reply_markup=keyboards.zero,
                                      parse_mode='markdown')
            else:
                return

    def send_order_info(self, chatid, lang):
        r = requests.post(config.site_base + 'ajax/ajaxCore.php',
                          data={'m': 'common', 'f': 'common_info', 'weight': self.weight})
        j = json.loads(r.text)
        if j['err'] == '1':
            main.bot.send_message(chatid, 'Internal error!', reply_markup=keyboards.zero)
            return_to_main_menu(chatid)
            return
        j = json.loads(j['msg'])
        ret = localization.get_message('n.your_order', lang) + "\n" + self.name + ',' + "\n" + self.phone + "\n" + str(
            self.weight) + "\n" + self.address + "\n" + localization.get_message('n.p' + str(self.payed),
                                                                                 lang) + "\n" + self.note + "\n`" + localization.get_message(
            'n.result', lang) + str(j['price']) + "`\n"
        main.bot.send_message(chatid, ret, reply_markup=keyboards.zero, parse_mode='markdown')
        main.bot.send_message(chatid, localization.get_message('n.tarif', lang) +
                              str(j['from']) + '-' + str(j['to']) +
                              localization.get_message('n.days', lang) +
                              str(j['selfCost']) +
                              localization.get_message('n.kg', lang),
                              reply_markup=keyboards.loc.get_keyboard('new_order_accept', lang))

    def handle_message(self, chatid, message):
        lang = db.get_lang(chatid)
        if self.substate == 0:
            self.name = message
            self.substate = 1
            main.bot.send_message(chatid, localization.get_message('n.phone', lang), reply_markup=keyboards.zero,
                                  parse_mode='markdown')
        elif self.substate == 1:
            if not(message.isdigit()):
                main.bot.send_message(chatid, 'Wrong phone format! Only digits without spaces or symbols!',
                                      reply_markup=keyboards.zero, parse_mode='markdown')
                return
            self.phone = message
            self.substate = 2
            main.bot.send_message(chatid, localization.get_message('n.weight', lang), reply_markup=keyboards.zero,
                                  parse_mode='markdown')
        elif self.substate == 2:
            if not(message.isdigit()):
                main.bot.send_message(chatid, 'Wrong weight!', reply_markup=keyboards.zero, parse_mode='markdown')
                return
            self.weight = int(message)
            self.substate = 3
            main.bot.send_message(chatid, localization.get_message('n.address', lang), reply_markup=keyboards.zero,
                                  parse_mode='markdown')
        elif self.substate == 3:
            self.address = message
            self.substate = 4
            main.bot.send_message(chatid, localization.get_message('n.payed', lang),
                                  reply_markup=keyboards.loc.get_keyboard('payed', lang), parse_mode='markdown')
        elif self.substate == 5:
            self.note = message
            self.substate = 10
            self.send_order_info(chatid, lang)


class MenuTrackState(StateCore):

    def handle_message(self, chatid, message):
        lang = db.get_lang(chatid)
        message = str(message)
        trackCode = message

        r = requests.post(config.site_base + 'ajax/ajaxCore.php',
                          data={'m': 'common', 'f': 'product_info', 'track_id': trackCode, 'lang': lang})
        j = {'err': '1'}
        try:
            j = json.loads(r.text)
        except:
            print('[Mishin870] Error in handle track while parse json: ' + str(r.text))
            main.bot.send_message(chatid, 'Internal error: ' + str(j['msg']), reply_markup=keyboards.zero)
            return_to_main_menu(chatid)
            return
        if j['err'] == '1':
            main.bot.send_message(chatid, 'Internal error: ' + str(j['msg']), reply_markup=keyboards.zero)
            return_to_main_menu(chatid)
            return
        j = json.loads(j['msg'])
        print(j)
        ret = localization.get_message('i.your_track', lang) + "\n" + str(j['name']) + "\n\n" + localization.get_message(
            'i.contacts', lang) + "\n" + "`" + str(j['phone']) + "`\n\n" + localization.get_message('i.tarif',
                                                                                                    lang) + str(
            j['from']) + '-' + str(j['to']) + localization.get_message('i.days', lang) + "\n"
        if int(j['payed']) == 1:
            ret += '`' + localization.get_message('i.pricey', lang) + str(j['price']) + '$' + "\n`"
        else:
            ret += '`' + localization.get_message('i.price', lang) + str(j['price']) + '$' + "\n`"
        ret += localization.get_message('i.weight', lang) + str(j['weight']) + ' ' + localization.get_message('n.kgs',
                                                                                                              lang) + "\n\n"
        pstate = int(j['state'])
        if pstate == 0:
            #головной офис
            ret += localization.get_message('i.office', lang) + "\n"
            ret += str(j['date']) + '. ' + localization.get_message('i.stambul', lang)
        elif pstate >= 1:
            #терр.
            ret += localization.get_message('i.terr', lang) + "\n"
            ret += str(j['date']) + '. ' + localization.get_message('i.tashkent', lang)

        main.bot.send_message(chatid, ret, reply_markup=keyboards.zero, parse_mode='markdown')
        return_to_main_menu(chatid)