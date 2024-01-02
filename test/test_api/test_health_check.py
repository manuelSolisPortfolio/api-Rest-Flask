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

from src.api.health_check.routes import Health
from test.test_api.helpers import create_server_app_client


class TestHealthCheck(TestCase):
    """Test the health check endpoint."""

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class.
        """
        cls.client = create_server_app_client(Health, "/health")

    def test_health_check(self):
        """
        Test if the health check endpoint returns the expected response.
        """
        response = self.client.get("/health")
        self.assertEqual(response.json, {"status": "OK"})
        self.assertEqual(response.status_code, 200)
