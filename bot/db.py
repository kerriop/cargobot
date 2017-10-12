states = {}
langs = {}

def setState(chatid, state):
    states[chatid] = state

def getState(chatid):
    return states.get(chatid)

def setLang(chatid, lang):
    langs[chatid] = lang

def getLang(chatid):
    lang = langs.get(chatid)
    if lang == None:
        return 'ru'
    else:
        return str(lang)