import os

from dotenv import load_dotenv

load_dotenv(".env")

class EnvVariables: 
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_NAME = os.environ.get("DB_NAME")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_COLLECTION = os.environ.get("DB_COLLECTION")
    DB_DRIVER = os.environ.get("DB_DRIVER")
