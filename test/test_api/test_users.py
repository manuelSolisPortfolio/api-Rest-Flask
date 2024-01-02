"""
Test users endpoints.

Tests:
    - GET /users : Should return a list of users from the database.
        Returns:
            - 200: OK.
                {
                    "status": "OK",
                    "data": [
                        {
                        "id": "1",
                        "name": "John Doe",
                        "email": "mail@example.com",
                        "password": "pass_example",
                        "created_at": "2021-01-01 00:00:00",
                        },
                        {...},
                    ]
                }
            -200 : OK. Whitout users
                {
                    "status": "OK",
                    "data": []
                }
    - GET /users/<id> : Should return a single user from the database.
        Returns:
            - 200: OK.
                {
                    "status": "OK",
                    "data": {
                        "id": "1",
                        "name": "John Doe",
                        "email": "main@example.com",
                        "password": "pass_example",
                        "created_at": "2021-01-01 00:00:00",
                    }
                }
            - 404: Not Found.
    - POST /users : Should create a new user into the database. 
            Constraints:
                -Unique users are allowed to be created.
                - Each new user will be added to the database with a unique id.
                - Each new user must have at least the information below.
                    Details: 
                        { 
                        "name": "John Doe",
                        "email": "john@example.com",
                        "password": "pass_example"
                        }
                - Additional parameters are allowed. Theses new parameters must not contain None or empty values.
                - The user must have unique email.

            Returns:
                - 201: Created: 
                    {
                        "status": "OK",
                        "data": {
                        "id": "1",
                        "name": "John Doe",
                        "email": "
                        "password": "pass_example",
                        "created_at": "2021-01-01 00:00:00",
                        }
                    }
                - 400: Bad Request.
                    Resquest with invalid parameters:
                        {
                            "status": "ERROR",
                            "message": "Invalid parameters."
                        }
                - 409: Conflict.
                    User already exists:
                        {
                            "status": "ERROR",
                            "message": "The user already exists."
                        }
                
    - PUT /users/<id>
        Constraints:
            - The user is already created.
            - Only valid data is allowed to be updated.
            -The modified user must at least have these parameters:
                { 
                        "name": "John Doe",
                        "email": "john@example.com",
                        "password": "pass_example"
                }
            - Additional parameters are allowed. Theses new parameters must not contain None or empty values.
        - 200: OK.
            {
                "status": "OK",
                "data": {
                    "id": "1",
                    "name": "John Doe",
                    "email": "mail@example",
                    "password": "pass_example",
                    "created_at": "2021-01-01 00:00:00",
                },
            }
    - DELETE /users/<id>
        - 204: No Content.
"""

from unittest import TestCase

from src.api.user.routes import Users
from test.test_api.helpers import create_server_app_client

ENDPOINT = "/users"


class TestUsers(TestCase):
    """Test users endpoints."""

    @classmethod
    def setUpClass(cls):
        """
        Set up the test class.
        """
        cls.client = create_server_app_client(Users, ENDPOINT)

    # def test_get_all_users(self):
    #     """Test get method."""
    #     response = self.client.get(ENDPOINT)
    #     self.assertEqual(response.json["status"], "OK")
    #     self.assertIsInstance(response.json["data"], list)
    #     self.assertEqual(response.status_code, 200)
