from unittest import TestCase
from server import app

class ServerTest(TestCase):
    def test_index(self):
        with app.test_client() as c:
            response = c.get('/')
            self.assertEqual(response.data, b'<h2>You have reached the Intersection Trivia API!</h2>')
            self.assertEqual(response.status_code, 200)