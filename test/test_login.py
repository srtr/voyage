from unittest import TestCase
from src.login import Login

class LoginTest(TestCase):
    def test_login_passes_with_valid_form(self):
        form = {'email': 'validemail@email.com', 'name': 'customer_1', 'mobile': 9000000000}
        self.assertEqual(Login().validate(form), True)

    def test_login_fails_with_numeric_emailId(self):
        # Make test fail
        form ={'email': 100}
        self.assertEqual(Login().validate(form), False)

    def test_login_fails_with_invalid_emailId(self):
        form = {'email': 'zzzz', 'name': 'customer_1', 'mobile': 9000000000}
        self.assertEqual(Login().validate(form), False)

    def test_login_fails_with_missing_emailId(self):
        form = {'name': 'customer_1', 'mobile': 9000000000}
        self.assertEqual(Login().validate(form), False)

    def test_login_fails_with_missing_name(self):
        form = {'email': 'abcdef@example.com', 'mobile': 9000000000}
        self.assertEqual(Login().validate(form), False)

    def test_login_fails_with_missing_mobile(self):
        form = {'email': 'abcdef@example.com', 'name': 'customer_1',}
        self.assertEqual(Login().validate(form), False)


    


