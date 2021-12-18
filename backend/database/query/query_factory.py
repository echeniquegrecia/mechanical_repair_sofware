from __future__ import annotations

import os
from abc import ABC
from abc import abstractmethod
from backend.database.connection.database_connection import DatabaseConnection
from backend.database.query.query import Sql
from backend.database.schema import CLIENTS
from backend.database.schema import VEHICLES_TYPE
from backend.database.schema import VEHICLES
from backend.database.schema import REPAIRS
from settings import DATABASE


class QueryFactoryAbs(ABC):
    """Query factory abstract class."""

    @abstractmethod
    def create(self, *args, **kwargs):
        """create query."""
        pass

    def invoke(self, *args, **kwargs):
        """Invoke query"""
        self.create(*args, **kwargs).execute()


class QueryFactory(QueryFactoryAbs):
    """Query Factory concrete class."""

    def __init__(self, database):
        """Query Factory init."""
        try:
            if not os.path.isfile(database):
                self.connection = DatabaseConnection(database_path=database)
                # Create tables iof the db does not exists.
                self.cursor = self.connection.get_cursor()
                self.cursor.execute(CLIENTS)
                self.cursor.execute(VEHICLES_TYPE)
                self.cursor.execute(VEHICLES)
                self.cursor.execute(REPAIRS)
            self.connection = DatabaseConnection(database_path=database)
            self.cursor = self.connection.get_cursor()
        except ConnectionError as error:
            raise error

    def create(self, query):
        """create query."""
        sql = Sql(cursor=self.cursor, query=query)
        return sql

