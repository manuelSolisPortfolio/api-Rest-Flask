"""Test mongo queries"""

from unittest import TestCase
from unittest.mock import Mock

from mongomock import MongoClient
from mongomock.collection import Cursor
from pymongo.collection import Collection

from src.database.mongodb.queries import MongoQueries


class TestMongoQueries(TestCase):
    """Test mongo queries."""

    def test_query_get_all(self):
        """Test get all users from database."""
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
        docs = queries.get_all()
        self.assertIsInstance(docs, Cursor)
        self.assertEqual(len(list(docs)), 2)
        self.assertEqual(docs[0]["name"], "John Doe")
        self.assertEqual(docs[1]["name"], "John Doe2")

    def test_queries_receives_invalid_collection(self):
        """Test if the queries receives valid collection."""

        with self.assertRaises(TypeError):
            MongoQueries(
                collection="invalid_collection",
            )
