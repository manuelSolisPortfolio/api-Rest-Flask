""" Test cases for the mongo database connector."""

from unittest import TestCase
from unittest.mock import patch

from mongomock import MongoClient
from mongomock.database import Database
from mongomock.collection import Collection

from src.database.mongodb.mongo_connector import MongoConnector
from src.database.mongodb.mongo_connector import get_mongo_connector


class TestMongoConnector(TestCase):
    """Test cases for the mongo database connector."""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up the mongo connector class."""
        cls.mongo_connector = MongoConnector(
            driver="mongodb",
            host="localhost",
            port=27017,
            database="mydatabase",
            collection="mycollection",
        )
    
    @patch("test.test_database.test_mongodb_connector.MongoConnector._create_client")
    def setUp(self, mock_client) -> None:
        """Set up the mongo connector."""
        mock_client.return_value = MongoClient()
        self.client = self.mongo_connector._create_client()
       

    def test_create_client(self):
        """Test if the client was created."""
        self.assertIsInstance(self.client, MongoClient)

    def test_create_database(self):
        """Test if the database was created."""
        database = self.mongo_connector._create_database(self.client)
        self.assertIsInstance(database, Database)

    
    def test_create_collection(self):
        """Test if the collection was created."""
        database = self.mongo_connector._create_database(self.client)
        collection = self.mongo_connector._create_collection(database)
        self.assertIsInstance(collection, Collection)

    @patch("test.test_database.test_mongodb_connector.MongoConnector._create_client")
    def test_connect(self, mock_client):
        """Test if the connection was successful."""
        mock_client.return_value = MongoClient()
        collection = self.mongo_connector.connect()
        self.assertIsInstance(collection, Collection)

    def test_get_mongo_connector(self) -> MongoConnector:
        """Return the mongo connector."""
        mongo_connector = get_mongo_connector()
        self.assertIsInstance(mongo_connector, MongoConnector)
