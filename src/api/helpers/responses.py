from flask import jsonify


class Response:

    """
    This class is used to create the responses of the API.

    """

    def ok_response_200(self, data: dict) -> dict:
        """
        This method is used to create the response of the API.

        Args:
            data (dict): data received from a request.

        Returns:
            dict: the response of the API.
        """

        return jsonify({"status": "ok", "data": data}), 200

    def ok_response_201(self, data: dict) -> tuple:
        return jsonify(
            {"status": "ok", "data": data}
        ), 201

    def ok_response_204(self) -> dict:
        return jsonify(
            {"status": "ok"}
        ), 204

    def bad_request_400(self, message: str) -> dict:
        return jsonify(
            {"status": "bad request", "message": message}
        ), 400

    def not_found_404(self, message: str) -> dict:
        return jsonify(
            {"status": "not found", "message": message}
        ), 404

    def internal_server_error_500(self, message: str) -> dict:
        return jsonify(
            {"status": "internal server error", "message": message}
        ), 500
