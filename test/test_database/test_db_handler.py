"""Test the database connection protocol implementation."""

from unittest import TestCase
from unittest.mock import Mock

from src.database.db_connector_protocol import DbConnectorProtocol
from src.database.handler import DatabaseHandler
from src.database.handler import get_db_handler


class TestDatabaseHandler(TestCase):
    "Test the database connection handler"

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class.
        """
        cls.db_connector_mock = Mock(spec=DbConnectorProtocol)
        cls.db_handler = DatabaseHandler(cls.db_connector_mock)

    def test_contains_connector(self):
        """
        Test if the handler contains a connector.
        """

        self.assertTrue(hasattr(self.db_handler, "connector"))

    def test_connector_is_db_connector_protocol(self):
        """
        Test if the connector is of type DbConnectorProtocol.
        """

        self.assertTrue(hasattr(self.db_handler.connector, "connect"))

    def test_connector_is_not_none(self):
        """
        Test if the connector is not None.
        """
        with self.assertRaises(ValueError, msg="Connector cannot be None."):
            DatabaseHandler(None)

    def test_connector_is_not_a_db_connector_protocol(self):
        """
        Test if the connector is not a DbConnectorProtocol.
        """
        with self.assertRaises(
            ValueError,
            msg="Connector must implement the DbConnectorProtocol.",
        ):
            DatabaseHandler("connector")

    def test_connect(self):
        """
        Test if the handler can connect to the database.
        """
        self.db_handler.connect()
        self.db_connector_mock.connect.assert_called_once()

    def test_get_db_handler(self):
        """Test if the get_db_handler function returns a DatabaseHandler instance."""
        db_handler = get_db_handler()
        self.assertIsInstance(db_handler, DatabaseHandler)
