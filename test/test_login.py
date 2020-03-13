from unittest import TestCase
from src.login import Login

class LoginTest(TestCase):
    def test_login_valid(self):
        form = {'email': 'abc@example.com'}
        self.assertEqual(Login.validate(form), True)

    def test_login_numeric(self):
        # Make test fail
        form ={'email': 100}
        self.assertEqual(Login.validate(form), False)
