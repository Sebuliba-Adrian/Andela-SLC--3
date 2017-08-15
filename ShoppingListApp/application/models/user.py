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

        if not len(items_list_title) > 9 and len(items_list_title) < 61:

            return "ItemsList name should be greater than 10 and less than 60 characters"






