"""Helper functions for testing the API."""

from flask import Flask
from flask_restful import Api, Resource


def create_server_app_client(resource_class: Resource, route: str):
    """
    Create a server app client for testing the API.
    
    Parameters:
        resource_class (Resource): The resource class of the endpoint.
        route (str): The route of the endpoint. E.g. "/users".
    
    Returns:
        Flask: The Flask client instance.
    """
    
    app = Flask(__name__)
    app.config["TESTING"] = True
    api = Api(app)
    api.add_resource(resource_class, route)
    return app.test_client()
