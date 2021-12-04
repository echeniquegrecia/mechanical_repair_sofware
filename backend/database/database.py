import os
import logging
import sqlite3

from backend.database.schema import CLIENTS
from backend.database.schema import VEHICLES_TYPE
from backend.database.schema import VEHICLES
from backend.database.schema import REPAIRS


class Singleton(type):
    """Singleton class for database."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnection(metaclass=Singleton):
    """DatabaseConnection class."""

    def __init__(self, database_path):
        """Database init."""
        self.database_path = database_path
        self.connection = self.get_connection()

    def get_connection(self):
        """Get Database connection."""
        try:
            if not os.path.isfile(self.database_path):
                # Create db and tables in case they do not exist.
                connection = sqlite3.connect(self.database_path)
                self.create_table(connection, CLIENTS)
                self.create_table(connection, VEHICLES_TYPE)
                self.create_table(connection, VEHICLES)
                self.create_table(connection, REPAIRS)
            connection = sqlite3.connect(self.database_path)
            logging.info("Database initialized.")
        except ConnectionError as error:
            logging.error(f"Database error: {error}.")
            raise error
        finally:
            connection.close()
        return connection

    def create_table(self, connection, table):
        """Create a table in Database."""
        try:
            connection.cursor().execute(table)
        except ConnectionError as error:
            logging.error(f"Database creation table error: {error}.")
            raise error

