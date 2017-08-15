import unittest
from application.models.user import User


class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("", "", "")

    def test_created_user(self):
        self.assertIsInstance(self.user, User, 'User not created')

    def test_add_itemsList_None(self):
        self.assertEqual(self.user.add_itemsList(None), "None input")

    def test_add_itemsList_blank_input(self):
        self.assertEqual(self.user.add_itemsList(" "), "Blank input")

    def test_add_itemsList_should_be_between10and60(self):
        self.assertEqual(self.user.add_itemsList("shortname"),
                         "ItemsList name should be greater than 10 and less than 60 characters")

        self.assertNotEqual(self.user.add_itemsList("long name long name long name long name long name long name long name"),
                         "ItemsListt name should be greater than 10 and less than 60 characters")





