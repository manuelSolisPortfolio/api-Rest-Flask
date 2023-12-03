"""Test the server application."""
from unittest import TestCase

from flask import Flask
from flask_restful import Api

from src.api.server import app


class TestServerApp(TestCase):

    """Test the server application."""

    def test_server_app(self):
        """
        Test if the server application is a Flask application.
        """
        self.assertIsInstance(app, Flask)

    # def test_api_server_app(self):
    #     """Test app of flask_restful_server"""
    #     self.assertIsInstance(api, Api)
