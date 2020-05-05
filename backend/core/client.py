class Client:
    """Class Client."""

    def __init__(self, connection):
        """Client init."""
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.sql = ""

    def get_all(self):
        """Get all the clients."""
        self.sql = "SELECT * FROM CLIENTS"
        self.cursor.execute(self.sql)
        values = list(self.cursor.fetchall())
        columns = list(map(lambda x: x[0], self.cursor.description))
        clients = [dict(zip(columns, value)) for value in values]
        clients = clients if clients else []
        return clients

    def get_by_id(self, client_id:int):
        """Get a client by client id."""
        self.sql = "SELECT * FROM CLIENTS WHERE client_id=?"
        values = list(self.cursor.execute(self.sql, (client_id,)))
        columns = list(map(lambda x: x[0], self.cursor.description))
        clients = [dict(zip(columns, value)) for value in values]
        return clients

    def get_by_name(self, name:str):
        """Get a client by name."""
        self.sql = "SELECT * FROM CLIENTS WHERE name=?"
        values = self.cursor.execute(self.sql, (name,))
        columns = list(map(lambda x: x[0], self.cursor.description))
        clients = [dict(zip(columns, value)) for value in values]
        return clients

    def get_by_last_name(self, last_name:str):
        """Get a client by last name."""
        self.sql = "SELECT * FROM CLIENTS WHERE last_name=?"
        values = self.cursor.execute(self.sql, (last_name,))
        columns = list(map(lambda x: x[0], self.cursor.description))
        clients = [dict(zip(columns, value)) for value in values]
        return clients

    def get_by_identity_card(self, identity_card:str):
        """Get a client by identity card."""
        self.sql = "SELECT * FROM CLIENTS WHERE identity_card=?"
        values = self.cursor.execute(self.sql, (identity_card,))
        columns = list(map(lambda x: x[0], self.cursor.description))
        clients = [dict(zip(columns, value)) for value in values]
        return clients

    def get_by_email(self, email:str):
        """Get a client by email."""
        self.sql = "SELECT * FROM CLIENTS WHERE email=?"
        values = self.cursor.execute(self.sql, (email,))
        columns = list(map(lambda x: x[0], self.cursor.description))
        clients = [dict(zip(columns, value)) for value in values]
        return clients

    def create(self, data:dict):
        """Create a client."""
        columns = ",".join([*data.keys()])
        values = list(data.values())
        placeholders = ','.join(['?'] * len(data))
        try:
            self.sql = f"INSERT INTO CLIENTS({columns}) VALUES({placeholders})"
            self.cursor.execute(self.sql, values)
            self.connection.commit()
            result = True
        except Exception:
            result = False
        return result

    def update(self, client_id: int, data:dict):
        """Update client details."""
        values = list(data.values())
        values.append(client_id)
        columns = list(data.keys())
        columns = [column + " = ?" for column in columns]
        columns = " , ".join(columns)
        try:
            self.sql = f"UPDATE CLIENTS SET {columns} WHERE client_id = ?"
            self.cursor.execute(self.sql, (values))
            self.connection.commit()
            result = True
        except Exception:
            result = False
        return result

    def delete(self, client_id: int):
        """Delete a client."""
        try:
            self.sql = "DELETE FROM CLIENTS WHERE client_id=?"
            self.cursor.execute(self.sql, (client_id,))
            self.connection.commit()
            result = True
        except Exception:
            result = False
        return result
