""" Users endpoints module."""

from typing import Any
from flask_restful import Resource

class Users(Resource):
    """Users endpoints class."""
    
    def __init__(self, service) -> None:
        """Constructor."""
        self.service = service

    def get(self):
        """Get all users."""
        data = self.service.get_all()
        return response.get(data=data)
