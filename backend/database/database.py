import os
import sqlite3

from backend.database.schema import CLIENTS
from backend.database.schema import VEHICLES_TYPE
from backend.database.schema import VEHICLES
from backend.database.schema import REPAIRS


class Database:

    def __init__(self, database: str):
        """Database init."""
        self.database = database
        self.connection = None

    def get_connection(self):
        """Get Database connection."""
        try:
            self.connection = sqlite3.connect(self.database)
            if not os.path.isfile(self.database):
                self.create_table(CLIENTS)
                self.create_table(VEHICLES_TYPE)
                self.create_table(VEHICLES)
                self.create_table(REPAIRS)
            return self.connection
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
