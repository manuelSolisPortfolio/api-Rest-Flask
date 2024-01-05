"""Module for health check endpoint."""

from http import HTTPStatus

from flask_restful import Resource


class Health(Resource):
    """Health check endpoint class."""

    def get(self):
        """Return the health check response."""
        return {"status": "OK"}, HTTPStatus.OK
