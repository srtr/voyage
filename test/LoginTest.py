import unittest
from src.Login import Login

class LoginTest(unittest.TestCase):
    def test_login(self):
        # Make test fail
        
        self.assertEqual(Login.validate(), 'Validate')
