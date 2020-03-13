from unittest import TestCase
from unittest.mock import MagicMock, patch
from data.client import DatabaseConnection, PollsClient

class PollsClientTest(TestCase):

    def test_get_polls(self):
        mock_polls = [{'a': 1234}]
        mock_conn, mock_collection = MagicMock(), MagicMock()

        mock_collection.find.return_value = mock_polls
        mock_conn().intersection.polls = mock_collection
        DatabaseConnection.get_connection = mock_conn

        client = PollsClient()
        self.assertEqual(client.get_polls(), mock_polls)
        mock_collection.find.assert_called_once_with()

    def test_get_poll_stats(self):
        mock_stats = [
            {"option": "A", "votes": 100},
            {"option": "B", "votes": 20},
	    ]
        mock_conn, mock_collection = MagicMock(), MagicMock()

        mock_collection.find_one.return_value = mock_stats
        mock_conn().intersection.polls = mock_collection
        DatabaseConnection.get_connection = mock_conn

        client = PollsClient()
        self.assertEqual(client.get_poll_stats('SOHO'), mock_stats)
        mock_collection.find_one.assert_called_once_with({'neighbourhood': 'SOHO'})
