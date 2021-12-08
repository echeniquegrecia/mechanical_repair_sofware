from __future__ import annotations
from abc import ABC
from abc import abstractmethod
from backend.database.connection.database_connection import DatabaseConnection


class QueryAbs(ABC):
    """Query abstract class."""

    @abstractmethod
    def execute(self, *args, **kwargs):
        """Execute query."""
        pass

    @abstractmethod
    def fetch(self):
        """Fetch query"""

    @abstractmethod
    def commit(self):
        """Commit query"""


class Sql(QueryAbs):
    """Sql class"""

    def __init__(self, cursor, query):
        """Sql init."""
        self.cursor = cursor
        self.query = query

    def execute(self):
        """Execute query sql."""
        try:
            self.cursor.execute(self.query)
        except Exception as error:
            raise error

    def fetch(self):
        """Fetch query."""
        try:
            self.cursor.fetchall()
        except Exception as error:
            raise error

    def commit(self):
        """Commit query"""
        try:
            self.cursor.commit()
        except Exception as error:
            raise error
