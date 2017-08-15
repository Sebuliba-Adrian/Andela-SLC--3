import unittest
from application.models.shoppingList import ItemsList

class ItemListTest(unittest.TestCase):

    def setUp(self):
        self.itemsList = ItemsList("")

    def test_itemsList_instantiation(self):
        self.assertIsInstance(self.itemsList, ItemsList, "Failed to instantiate")

    # def test_update_none_input(self, description, new_description):
    #     self.assertEqual(self.itemsList.update_bucket(" ", "  "), "Blank input")




