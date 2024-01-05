# import functools


# class Validations:
#     @staticmethod
#     def _is_valid_type(data: dict) -> bool:
#         return isinstance(data, dict)
#         return (
#             {"data_structure_error": "Data must be a dictionary"}
#             if not isinstance(data, dict)
#             else None
#         )

#     @staticmethod
#     def _is_empty(data: dict) -> bool:
#         return not data
#         return {"content_error": "Data must not be empty"} if not data else None

#     # @classmethod
#     # def validate_body(cls, data: dict):
#     #     cls._validate_dict_structure(data)
#     #     cls._validate_content(data)

#     @staticmethod
#     def validate_body_decorator(function: callable):
#         @functools.wraps(function)
#         def wrapped(*args, **kwargs):
#             breakpoint()
#             data = kwargs.get("data")
#             errors = {"errors": None}

#             if not Validations._is_valid_type(data):
#                 errors["errors"] = [
#                     {"data_structure_error": "Data must be a dictionary"}
#                 ]
#             if Validations._is_empty(data):
#                 errors["errors"] = [
#                     {"content_error": "Data must not be empty"}]
#             breakpoint()
#             if errors["errors"]:
#                 return errors, 400
#             return function(*args, **kwargs)

#         return wrapped
