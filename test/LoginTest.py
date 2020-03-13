import unittest
from src.Login import Login

class LoginTest(unittest.TestCase):
    def test_login(self):
        # Make test fail
        form = []
        form['email'] = 100
        self.assertEqual(Login.validate(form), true)
