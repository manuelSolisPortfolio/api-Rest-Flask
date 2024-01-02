""" Main module of the application. """

from src.api.server import run_application
# from src.database.handler import get_db_handler

if __name__ == "__main__":
    # database_handler = get_db_handler()
    # database_handler.connect()
    run_application()
