import logging
import sqlite3


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
        """Get database connection."""
        try:
            connection = sqlite3.connect(self.database_path)
            logging.info("Connecting to database.")
        except ConnectionError as error:
            logging.error(f"Database error: {error}.")
            raise error
        finally:
            sqlite3.connect(self.database_path).close()
        return connection

    def get_cursor(self):
        """Get cursor."""
        try:
            cursor = self.connection.cursor()
        except ConnectionError as error:
            raise error
        return cursor

    def close(self):
        """Close cursor."""
        try:
            self.connection.close()
        except ConnectionError as error:
            raise error
