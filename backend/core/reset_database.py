class ResetDatabase:
    """Class Client."""

    def __init__(self, connection):
        """Client init."""
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.sql = None
        self.sql = "DROP "

        self.cursor.execute(self.sql)
