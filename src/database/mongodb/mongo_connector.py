"""This module is responsible for creating a connection with MongoDB."""
import logging

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

from env_variables import EnvVariables

logs = logging.getLogger(__name__)


class MongoConnector:
    """Class responsible for creating a connection with MongoDB."""

    def __init__(
        self,
        driver: str,
        host: str,
        port: int,
        database: str,
        collection: str,
    ) -> None:
        """
        Initialize the class with the necessary attributes.

        params:
            driver (str): Driver to connect with MongoDB.
            host (str): Host to connect with MongoDB.
            port (int): Port to connect with MongoDB.
            database (str): Database to connect with MongoDB.
            collection (str): Collection to connect with MongoDB.
        """
        self.driver = driver
        self.host = host
        self.port = port
        self.database = database
        self.collection = collection

    def _create_client(self):
        """Create a client to connect with MongoDB."""
        logs.info("Creating a client to connect with DB.")
        return MongoClient(f"{self.driver}://{self.host}:{self.port}/")

    def _create_database(self, client: MongoClient) -> Database:
        """
        Create a database to connect with MongoDB.
            params:
               client: MongoClient object.
            return:
                MongoDatabase object.

        """
        logs.info("Creating a database.")
        return client[self.database]

    def _create_collection(self, database: Database) -> Collection:
        """
        Create a collection to connect with MongoDB.

        Args:
            database (Database): mongo_database object.

        Returns:
            collection: mongo_collection object.
        """
        logs.info("Creating a collection.")
        return database[self.collection]

    def connect(self) -> MongoClient:
        """
        Connect with MongoDB.
        return:
            MongoCollection object.
        """
        logs.info("Connecting with MongoDB.")
        client = self._create_client()
        database = self._create_database(client)
        self._create_collection(database)
        return client
