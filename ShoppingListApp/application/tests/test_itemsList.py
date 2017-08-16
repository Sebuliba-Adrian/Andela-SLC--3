import unittest
from application.models.shoppingList import ItemsList

class ItemListTest(unittest.TestCase):

    def setUp(self):
        self.itemsList = ItemsList("")

    def test_itemsList_instantiation(self):
        self.assertIsInstance(self.itemsList, ItemsList, "Failed to instantiate")

    def test_add_item_none(self):
       self.assertEqual(self.itemsList.add_item(None), "None input")

    def test_add_item_blank(self):
        self.assertEqual(self.itemsList.add_item(" "), "Blank input")

    def test_add_item_added(self):
        self.assertEqual(self.itemsList.add_item("mangoes"), "Item added")

    def test_add_item_exists(self):
        self.itemsList.add_item("mangoes")
        self.assertEqual(self.itemsList.add_item("mangoes"), "Item already exists")










