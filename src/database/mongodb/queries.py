"""Module of mongo queries."""

import logging

from pymongo.collection import Collection, Cursor

logs = logging.getLogger(__name__)


class MongoQueries:
    """Mongo queries class."""

    def __init__(
        self,
        collection: Collection,
    ) -> None:
        """Constructor."""
        logs.info("Constructing MongoQueries.")
        self.collection = collection

    @property
    def collection(self) -> Collection:
        """Return the collection property."""
        return self._collection

    @collection.setter
    def collection(self, new_collection: Collection):
        """Set the collection property."""
        logs.info("Setting collection.")
        if not isinstance(new_collection, Collection):
            raise TypeError("Collection must be a Collection instance.")
        self._collection = new_collection

    def get_all(self) -> Cursor:
        """Get all items."""
        logs.info("Getting all registers from %s.", self.collection.name)
        return self.collection.find()
