import unittest
from application.models.shoppingList import ItemsList


class ItemListTest(unittest.TestCase):

    def setUp(self):
        self.itemsList = ItemsList("")

    def test_itemsList_instantiation(self):
        self.assertIsInstance(self.itemsList, ItemsList,
                              "Failed to instantiate")

    def test_add_item_none(self):
        self.assertEqual(self.itemsList.add_item(None), "None input")

    def test_add_item_blank(self):
        self.assertEqual(self.itemsList.add_item(" "), "Blank input")

    def test_add_item_added(self):
        self.assertEqual(self.itemsList.add_item("mangoes"), "Item added")

    def test_add_item_exists(self):
        self.itemsList.add_item("mangoes")
        self.assertEqual(self.itemsList.add_item(
            "mangoes"), "Item already exists")



    def test_update_description_none(self):
        self.assertEqual(self.itemsList.update_description(None, None), "None input")

    def test_update_description_blank(self):
        self.assertEqual(self.itemsList.update_description(" ", " "), "Blank input")

    def test_update_description_no_changes(self):
        self.assertEqual(self.itemsList.update_description(
            "Yello Mango", "Yello Mango"), "No changes")

    def test_update_description_not_found(self):
        self.assertEqual(self.itemsList.update_description(
            "Green mango", "Green Mango"), "Item not found")

    