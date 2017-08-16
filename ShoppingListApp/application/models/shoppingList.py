
from application.models.item import Item
class ItemsList(object):
    def __init__(self, title):
        self.title = title
        self.items = {}


    def add_item(self, description):
        """ Adds an Item to a items """
        if description:
            if description.strip():
                if not description in self.items:
                    self.items[description] = Item(description)
                    return "Item added"
                return "Item already exists"
            return "Blank input"
        return "None input"







