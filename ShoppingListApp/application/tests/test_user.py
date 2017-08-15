import unittest
from application.models.user import User

class UserTest(unittest.TestCase):
    def setUp(self):
        self.user = User("","","")


    def test_add_itemsList(self):
         self.assertEqual(self.user.add_itemsList(None), "None input")








