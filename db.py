states = {}
langs = {}


def set_state(chatid, state):
    states[chatid] = state


def get_state(chatid):
    return states.get(chatid)


def set_lang(chatid, lang):
    langs[chatid] = lang


def get_lang(chatid):
    lang = langs.get(chatid)
    if lang is None:
        return 'ru'
    else:
        return str(lang)
