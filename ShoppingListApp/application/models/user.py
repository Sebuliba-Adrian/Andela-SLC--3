class User(object):
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.itemsList = {}


    def add_itemsList(self,items_list_title):

        if not items_list_title:
            return "None input"

        if not items_list_title.strip():

            return "Blank input"




