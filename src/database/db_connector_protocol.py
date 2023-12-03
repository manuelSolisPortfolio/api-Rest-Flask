""" Database Connector Protocol """

from typing import Protocol


class DbConnectorProtocol(Protocol):

    """Database Connection Protocol"""

    def __init__(self) -> None:
        """Constructor for the Database Connection Protocol."""
        pass

    def connect(self):
        """Method for connecting to a database."""
        pass
