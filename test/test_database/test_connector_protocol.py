"""This module contains tests for the connector protocol."""

from typing import Protocol
from unittest import TestCase

from src.database.db_connector_protocol import DbConnectorProtocol


class TestConnectorProtocol(TestCase):

    """This module contains tests for the connector protocol."""

    def test_connector_protocol(self):
        """Test if the connector protocol is a Protocol."""
        self.assertTrue(issubclass(DbConnectorProtocol, Protocol))

    def test_connector_protocol_has_connect_method(self):
        """Test if the connector protocol has a connect method."""
        self.assertTrue(hasattr(DbConnectorProtocol, "connect"))
        DbConnectorProtocol().connect()
        self.assertTrue(callable(DbConnectorProtocol.connect))

    def test_connector_protocol_has_init_method(self):
        """Test if the connector protocol has an init method."""
        self.assertTrue(hasattr(DbConnectorProtocol, "__init__"))
        DbConnectorProtocol().__init__()
        self.assertTrue(callable(DbConnectorProtocol.__init__))
