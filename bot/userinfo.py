class UserInfo(object):
    def __init__(self):
        self.name = ''

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


users = {}

def addUser(chatid):
    users[chatid] = UserInfo()

def getUser(chatid):
    return users.get(chatid)