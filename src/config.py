from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
ODB_HOST = os.environ.get("ODB_HOST")
ODB_PORT = os.environ.get("ODB_PORT")
ODB_USER = os.environ.get("ODB_USER")
ODB_PASSWORD = os.environ.get("ODB_PASSWORD")
ODB_NAME = os.environ.get("ODB_NAME")


# SQLALCHEMY_DB_URL=f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'