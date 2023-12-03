"""
This module test the health check endpoint.
The get method should return the expected response.
Response:
    {
        "status": "OK"
    }
    status_code: 200
"""
from unittest import TestCase

from flask import Flask
from flask_restful import Api

from src.api.health_check.routes import Health


class TestHealthCheck(TestCase):
    """Test the health check endpoint."""

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class.
        """
        app = Flask(__name__)
        app.config["TESTING"] = True
        api = Api(app)
        api.add_resource(Health, "/health")
        cls.client = app.test_client()

    def test_health_check(self):
        """
        Test if the health check endpoint returns the expected response.
        """
        response = self.client.get("/health")
        self.assertEqual(response.json, {"status": "OK"})
        self.assertEqual(response.status_code, 200)
