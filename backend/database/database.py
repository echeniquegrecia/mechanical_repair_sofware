import os
import sqlite3


class Database:

    def __init__(self, database: str):
        """Database init."""
        self.database = database
        self.connection = None

    def get_connection(self):
        """Get Database connection."""
        try:
            if os.path.isfile(self.database):
                connection = sqlite3.connect(self.database)
            else:
                connection = sqlite3.connect(self.database)
            self.connection = connection
            return connection
        except ConnectionError as error:
            return error
        finally:
            sqlite3.connect(self.database).close()


    def create_table(self, table):
        """Create a table."""
        try:
            self.connection.cursor().execute(table)
        except ConnectionError as error:
            return error
