from pymongo import MongoClient

class DatabaseConnection(object):
    _conn = None

    @classmethod
    def get_connection(cls):
        if cls._conn is None:
            cls._conn = MongoClient("mongodb://localhost:27017")
        return cls._conn


class PollsClient(object):
    def __init__(self):
        self.conn = DatabaseConnection.get_connection()
        self.collection = self.conn.intersection.polls

    def get_polls(self):
        return self.collection.find()

    def get_poll_stats(self, neighbourhood):
        return self.collection.find_one({'neighbourhood': neighbourhood})

polls_client = PollsClient()
