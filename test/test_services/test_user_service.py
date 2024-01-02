"""
Test user service.

Tests:
    - get_all: Should return a list of users from the database.
        Returns:
            [
                {
                "id": "1",
                "name": "John Doe",
                "email": "mail@example.com",
                "password": "pass_example",
                "created_at": "2021-01-01 00:00:00",
                },
                {...},
            ]
"""

from unittest import TestCase
from unittest.mock import Mock

from pymongo.collection import Collection
from mongomock import MongoClient

from src.database.mongodb.queries import MongoQueries
from src.api.user.user_service import UserService

class TestUserService(TestCase):
    "Test user service methods."

    def test_user_service_get_all(self):
        "Test get all users."
        mongo_client = MongoClient()
        database = mongo_client["test_database"]
        collection = database["test_collection"]
        collection_mock = Mock(spec=Collection)
        collection_mock.find = collection.find
        queries = MongoQueries(
            collection=collection_mock,
        )
        docs = queries.get_all()
        self.assertEqual(len(list(docs)), 0)
        collection.insert_one({"name": "John Doe"})
        collection.insert_one({"name": "John Doe2"})
        user_service = UserService(queries=queries)
        users = user_service.get_all()
        self.assertEqual(len(users), 2)
        self.assertIsInstance(users, list)
        self.assertEqual(users[0]["name"], "John Doe")
        self.assertEqual(users[1]["name"], "John Doe2")
