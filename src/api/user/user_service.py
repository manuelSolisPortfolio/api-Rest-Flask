"""
User service that provides the business logic for the user endpoints.

This module provides the bridge interface between the user endpoints and the database.
"""


class UserService:
    """User service class."""

    def __init__(self, queries) -> None:
        """Constructor."""
        self.queries = queries

    def get_all(self) -> list:
        """Get all users."""
        items = self.queries.get_all()
        return [item for item in items]
