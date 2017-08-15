from application.models.shoppingList import ItemsList


class User(object):
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        self.itemsList = {}

    def add_itemsList(self, items_list_title):
        if items_list_title:
            if items_list_title.strip():
                if len(items_list_title) > 9 and len(items_list_title) < 61:
                    if not items_list_title in self.itemsList:
                        self.itemsList[items_list_title] = ItemsList(
                            items_list_title)
                        return "ItemsList added"
                    return "An ItemsList with this name already exists"
                return "ItemsList name should be greater than 10 and less than 60 characters"
            return "Blank input"
        return "None input"
