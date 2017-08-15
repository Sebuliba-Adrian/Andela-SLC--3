import unittest
from application.models.user import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("Adrian", "adris", "secret")

    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')

    def test_add_itemsList_None(self):
        self.assertEqual(self.user.add_itemsList(None), "None input")

    def test_add_itemsList_blank_input(self):
        self.assertEqual(self.user.add_itemsList(" "), "Blank input")

    def test_add_itemsList_should_be_between10and60(self):
        self.assertEqual(self.user.add_itemsList("shortname"),
                         "ItemsList name should be greater than 10 and less than 60 characters")

        self.assertEqual(self.user.add_itemsList("long name long name long name long name long name long name long name"),
                         "ItemsList name should be greater than 10 and less than 60 characters")

    def test_add_itemsList_bucket_added(self):
        self.assertEqual(self.user.add_itemsList("Furnitures"),
                         "ItemsList added")

    def test_add_itemsList_name_already_exists(self):
        self.user.add_itemsList("Furnitures")
        self.assertEqual(self.user.add_itemsList
                         ("Furnitures"),
                         "An ItemsList with this name already exists")

    def test_update_ItemsList_None(self):
        self.assertEqual(self.user.update_ItemsList(None, None), "None input")


    def test_update_ItemsList_blank(self):
        self.assertEqual(self.user.update_ItemsList(" ", " "), "Blank input")

    def test_update_ItemsList_same_name(self):
       self.assertEqual(self.user.update_ItemsList("Fruits",
                                                 "Fruits"),
                         "No change, same name")

    def test_update_ItemsList_not_found(self):
        self.assertEqual(self.user.update_ItemsList("notinthelistofitemList", "snewname"),
                         "ItemsList not found")

    def test_update_ItemsList_no_change(self):
        self.user.add_itemsList("Stationary")
        self.user.add_itemsList("Electronics")

        self.assertEqual(self.user.update_ItemsList("Electronics",
                                                 "Stationary"),
                         "No change, new name already in itemsList")


    def test_update_ItemsList_updated(self):
        self.user.add_itemsList("Drinks and Beer")

        self.assertEqual(self.user.update_ItemsList("Drinks and Beer",
                                                 "Clothes and Dresses"),
                         "ItemsList updated")

    def test_delete_itemsList(self):
        pass
