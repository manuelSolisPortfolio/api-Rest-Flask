"""This module contains the implementation of the database connection protocol."""

import logging

from src.database.db_connector_protocol import DbConnectorProtocol

logs = logging.getLogger(__name__)
DatabaseClient=object


class DatabaseHandler:
    "This is the database connection handler."

    def __init__(self, connector: DbConnectorProtocol):
        """
        Initialize the class with the necessary attributes.

        params:
            connector(DbConnectorProtocol): The database connector.
        """
        self.connector = connector

    @property
    def connector(self) -> DbConnectorProtocol:
        """
        Return the database connector property.

        Returns:
            DbConnectorProtocol: The database connector instance.

        """
        return self._connector

    @connector.setter
    def connector(self, new_connector: DbConnectorProtocol):
        """
        Set the database connector property.

        Parameters:
            new_connector (DbConnectorProtocol): The new database connector.

        Raises:
            ValueError: If new_connector does not implement the DbConnectorProtocol.
            ValueError: If new_connector is None.
        """
        if not new_connector:
            raise ValueError("Connector cannot be None.")

        if not hasattr(new_connector, "connect"):
            raise ValueError("Connector must implement the DbConnectorProtocol.")
        logs.info("Connector is set.")
        self._connector = new_connector

    def connect(self) -> DatabaseClient:
        """Connect to the database."""
        logs.info("Connecting to the database.")
        return self.connector.connect()
