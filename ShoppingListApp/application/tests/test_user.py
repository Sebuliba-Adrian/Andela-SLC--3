import unittest
from application.models.user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("","","")


    def test_add_itemsList_None(self):
         self.assertEqual(self.user.add_itemsList(None), "None input")

    def test_add_itemsList_blank_input(self):
        self.assertEqual(self.user.add_itemsList(" "), "Blank input")








