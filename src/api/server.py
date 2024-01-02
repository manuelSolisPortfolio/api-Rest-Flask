"""This module contains the server application configuration."""

from flask import Flask
from flask_restful import Api

from src.api.health_check.routes import Health
from src.api.user.routes import Users

app = Flask(__name__)
api = Api(app)


def register_routes():
    """Register the routes of the application."""
    api.add_resource(Health, "/health")
    api.add_resource(Users, "/users")


def run_application(debug_mode: bool = True):
    """
    Run the application with the given configuration.

    Parameters:
        debug_mode (bool): The debug mode of the application. Defaults to True.
    """
    register_routes()
    app.run(debug=debug_mode, host="127.0.0.1")
