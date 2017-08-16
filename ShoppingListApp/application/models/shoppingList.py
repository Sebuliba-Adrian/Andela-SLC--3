
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

    def update_description(self, description, new_description):
        """ Updates an Item's description in a bucket """
        if description and new_description:
            if description.strip() and new_description.strip:
                if not new_description == description:
                    if not new_description in self.items:
                        if description in self.items:
                            self.items[new_description] = self.items.pop(
                                description)
                            pass
                        pass
                    pass
                return "No changes"
            return "Blank input"
        return "None input"
