from backend.exceptions.client_exceptions import ClientDeleteException
from backend.exceptions.client_exceptions import ClientUpdateException
from backend.exceptions.client_exceptions import ClientCreateException
from backend.exceptions.client_exceptions import ClientGetCategoryException
from backend.exceptions.client_exceptions import ClientGetAllException
from backend.exceptions.client_exceptions import ClientFormatDataException
from backend.service.check_client_data import CheckClientDataFormat
from backend.service.convert_uppercase import convert_uppercase


class Client:
    """Class Client."""

    def __init__(self, connection):
        """Client init."""
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.sql = None

    def get_all(self):
        """Get all the clients."""
        try:
            self.sql = "SELECT * FROM CLIENTS"
            self.cursor.execute(self.sql)
            values = list(self.cursor.fetchall())
        except Exception:
            raise ClientGetAllException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        clients = [dict(zip(columns, value)) for value in values]
        return clients

    def get_by_id(self, client_id: int):
        """Get a client by client id."""
        try:
            self.sql = "SELECT * FROM CLIENTS WHERE client_id=?"
            values = list(self.cursor.execute(self.sql, (client_id,)))
        except Exception:
            raise ClientGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        clients = [dict(zip(columns, value)) for value in values]
        return clients

    def get_by_name(self, name: str):
        """Get a client by name."""
        name = convert_uppercase(param=name)
        try:
            self.sql = "SELECT * FROM CLIENTS WHERE name=?"
            values = self.cursor.execute(self.sql, (name,))
        except Exception:
            raise ClientGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        clients = [dict(zip(columns, value)) for value in values]
        return clients

    def get_by_last_name(self, last_name: str):
        """Get a client by last name."""
        last_name = convert_uppercase(param=last_name)
        try:
            self.sql = "SELECT * FROM CLIENTS WHERE last_name=?"
            values = self.cursor.execute(self.sql, (last_name,))
        except Exception:
            raise ClientGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        clients = [dict(zip(columns, value)) for value in values]
        return clients

    def get_by_identity_card(self, identity_card: str):
        """Get a client by identity card."""
        identity_card = convert_uppercase(param=identity_card)
        try:
            self.sql = "SELECT * FROM CLIENTS WHERE identity_card=?"
            values = self.cursor.execute(self.sql, (identity_card,))
        except Exception:
            raise ClientGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        clients = [dict(zip(columns, value)) for value in values]
        return clients

    def get_by_email(self, email: str):
        """Get a client by email."""
        email = convert_uppercase(param=email)
        try:
            self.sql = "SELECT * FROM CLIENTS WHERE email=?"
            values = self.cursor.execute(self.sql, (email,))
        except Exception:
            raise ClientGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        clients = [dict(zip(columns, value)) for value in values]
        return clients

    def create(self, **kwargs):
        """Create a client

         **kwargs:
        name: client name
        last_name: client last name
        identity_card: client identity card
        email: client email
        phone_1: client phone 1
        phone_2: client phone 2
        address: client address.
        """
        try:
            CheckClientDataFormat(client_data=kwargs)
        except ClientFormatDataException as error:
            raise ClientFormatDataException(message=error.message)
        kwargs = convert_uppercase(param=kwargs)
        columns = ",".join([*kwargs.keys()])
        values = list(kwargs.values())
        placeholders = ','.join(['?'] * len(kwargs))
        try:
            self.sql = f"INSERT INTO CLIENTS({columns}) VALUES({placeholders})"
            self.cursor.execute(self.sql, values)
            self.connection.commit()
        except Exception:
            raise ClientCreateException()

    def update(self, **kwargs):
        """Update client details

        **kwargs:
        id: client id
        name: client name
        last_name: client last name
        identity_card: client identity card
        email: client email
        phone_1: client phone 1
        phone_2: client phone 2s
        address: client address.
        """
        try:
            CheckClientDataFormat(client_data=kwargs)
        except ClientFormatDataException as error:
            raise ClientFormatDataException(message=error.message)
        kwargs = convert_uppercase(param=kwargs)
        values = list(kwargs.values())
        values.append(kwargs.get("client_id"))
        columns = list(kwargs.keys())
        columns = [column + " = ?" for column in columns]
        columns = " , ".join(columns)
        try:
            self.sql = f"UPDATE CLIENTS SET {columns} WHERE client_id = ?"
            self.cursor.execute(self.sql, values)
            self.connection.commit()
        except Exception:
            raise ClientUpdateException()

    def delete(self, client_id: int):
        """Delete a client."""
        self.sql = "SELECT * FROM VEHICLES WHERE client_id=?"
        values = self.cursor.execute(self.sql, (client_id,))
        response = [value for value in values]
        if response:
            error_message = "The client contains a vehicle registered."
            raise ClientDeleteException(message=error_message)
        try:
            self.sql = "DELETE FROM CLIENTS WHERE client_id=?"
            self.cursor.execute(self.sql, (client_id,))
            self.connection.commit()
        except Exception:
            raise ClientDeleteException()
