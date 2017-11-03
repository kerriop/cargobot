class UserInfo(object):
    def __init__(self):
        self.name = ''

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


users = {}

def add_user(chatid):
    users[chatid] = UserInfo()

def get_user(chatid):
    return users.get(chatid)