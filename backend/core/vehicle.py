import sqlite3

from backend.exceptions.vehicle_exceptions import VehicleDeleteException, VehicleUpdateException, \
    VehicleCreateException, VehicleGetAllException, VehicleGetCategoryException
from backend.service.check_vehicle_data import CheckVehicleDataFormat
from backend.service.convert_uppercase import convert_uppercase


class Vehicle:
    """Class Vehicle."""

    def __init__(self, connection):
        """Vehicle init."""
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.sql = ""

    def get_all(self):
        """Get all vehicles."""
        try:
            self.sql = "SELECT * FROM VEHICLES"
            self.cursor.execute(self.sql)
            values = list(self.cursor.fetchall())
        except Exception:
            raise VehicleGetAllException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_by_id(self, vehicle_id: int):
        """Get vehicle by vehicle_id."""
        try:
            self.sql = "SELECT * FROM VEHICLES WHERE vehicle_id=?"
            values = self.cursor.execute(self.sql, (vehicle_id,))
        except Exception:
            raise VehicleGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_by_client_id(self, client_id: int):
        """Get vehicle by client id."""
        try:
            self.sql = "SELECT * FROM VEHICLES WHERE client_id=?"
            values = self.cursor.execute(self.sql, (client_id,))
        except Exception:
            raise VehicleGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_by_vehicle_type_id(self, vehicle_type_id: int):
        """Get vehicle by vehicle type id."""
        try:
            self.sql = "SELECT * FROM VEHICLES WHERE vehicle_type_id=?"
            values = self.cursor.execute(self.sql, (vehicle_type_id,))
        except Exception:
            raise VehicleGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_by_identity(self, identity: int):
        """Get vehicle by identity."""
        try:
            self.sql = "SELECT * FROM VEHICLES WHERE identity=?"
            values = self.cursor.execute(self.sql, (identity,))
        except Exception:
            raise VehicleGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_by_color(self, color: str):
        """Get vehicle by color."""
        try:
            self.sql = "SELECT * FROM VEHICLES WHERE color=?"
            values = self.cursor.execute(self.sql, (color,))
        except Exception:
            raise VehicleGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_by_vehicle_type_id_with_details(self, vehicle_id: int):
        """Get vehicle by vehicle type id."""
        try:
            self.sql = "" \
                       "SELECT VEHICLES.vehicle_id," \
                       "identity," \
                       "color," \
                       "brand," \
                       "model," \
                       "year " \
                       "FROM VEHICLES " \
                       "INNER JOIN VEHICLES_TYPE ON VEHICLES_TYPE.vehicle_type_id = VEHICLES.vehicle_type_id " \
                       f"WHERE VEHICLES.vehicle_id = ?;"
            self.cursor.execute(self.sql, (vehicle_id,))
            values = list(self.cursor.fetchall())
        except Exception:
            raise VehicleGetCategoryException()
        columns = ["vehicle_id", "identity", "color", "brand", "model", "year"]
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_vehicles_with_type_details(self):
        """Get vehicles with type details."""
        try:
            self.sql = "" \
                       "SELECT VEHICLES.vehicle_id," \
                       "identity," \
                       "color," \
                       "brand," \
                       "model," \
                       "year " \
                       "FROM VEHICLES "\
                       "INNER JOIN VEHICLES_TYPE ON VEHICLES_TYPE.vehicle_type_id = VEHICLES.vehicle_type_id;"
            self.cursor.execute(self.sql)
            values = list(self.cursor.fetchall())
        except Exception:
            raise VehicleGetCategoryException()
        columns = ["vehicle_id", "identity", "color", "brand", "model", "year"]
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_vehicles_with_clients_details(self):
        """Get vehicles with clients details."""
        try:
            self.sql = "" \
            "SELECT VEHICLES.vehicle_id ," \
                    "VEHICLES.identity AS vehicle_identity," \
                    "VEHICLES.color AS color," \
                    "VEHICLES_TYPE.model AS model," \
                    "VEHICLES_TYPE.brand AS brand," \
                    "VEHICLES_TYPE.year AS year," \
                    "CLIENTS.client_id as client_id," \
                    "CLIENTS.name as client_name," \
                    "CLIENTS.last_name as client_last_name," \
                    "CLIENTS.identity_card as client_identity " \
                    "FROM VEHICLES_TYPE " \
            "INNER JOIN VEHICLES ON VEHICLES.vehicle_type_id = VEHICLES_TYPE.vehicle_type_id " \
            "INNER JOIN CLIENTS ON CLIENTS.client_id = VEHICLES.client_id;"
            self.cursor.execute(self.sql)
            values = list(self.cursor.fetchall())
        except Exception:
            raise VehicleGetCategoryException()
        columns = [
            "vehicle_id",
            "vehicle_identity",
            "color",
            "model",
            "brand",
            "year",
            "client_id",
            "client_name",
            "client_last_name",
            "client_identity"
        ]
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_vehicles_by_category(self, category: str, value):
        """Get vehicles by a category specific with client details."""
        try:
            self.sql = "" \
                       "SELECT VEHICLES.vehicle_id ," \
                       "VEHICLES.identity AS vehicle_identity," \
                       "VEHICLES.color AS color," \
                       "VEHICLES_TYPE.model AS model," \
                       "VEHICLES_TYPE.brand AS brand," \
                       "VEHICLES_TYPE.year AS year," \
                       "CLIENTS.client_id as client_id," \
                       "CLIENTS.name as client_name," \
                       "CLIENTS.last_name as client_last_name," \
                       "CLIENTS.identity_card as client_identity " \
                       "FROM VEHICLES_TYPE " \
                       "INNER JOIN VEHICLES ON VEHICLES.vehicle_type_id = VEHICLES_TYPE.vehicle_type_id " \
                       "INNER JOIN CLIENTS ON CLIENTS.client_id = VEHICLES.client_id " \
                       f"WHERE {category} =?;"
            self.cursor.execute(self.sql, (value,))
            values = list(self.cursor.fetchall())
        except Exception:
            raise VehicleGetCategoryException()
        columns = [
            "vehicle_id",
            "vehicle_identity",
            "color",
            "model",
            "brand",
            "year",
            "client_id",
            "client_name",
            "client_last_name",
            "client_identity"
        ]
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def create(self, **kwargs):
        """Create a vehicle.

        **kwargs:
        vehicle_type_id: Vehicle type ID
        identity": Identity of the vehicle
        color: Vehicle color
        """
        kwargs = convert_uppercase(param=kwargs)
        CheckVehicleDataFormat(kwargs)
        columns = ",".join([*kwargs.keys()])
        values = list(kwargs.values())
        placeholders = ','.join(['?'] * len(kwargs))
        try:
            self.sql = f"INSERT INTO VEHICLES({columns}) VALUES({placeholders})"
            self.cursor.execute(self.sql, values)
            self.connection.commit()
        except sqlite3.IntegrityError:
            raise sqlite3.IntegrityError()
        except Exception:
            raise VehicleCreateException()

    def update(self, vehicle_id: int, **kwargs):
        """Update client details

        **kwargs:
        vehicle_type_id: Vehicle type ID
        identity": Identity of the vehicle
        color: Vehicle color
        """
        kwargs = convert_uppercase(param=kwargs)
        CheckVehicleDataFormat(kwargs)
        values = list(kwargs.values())
        values.append(vehicle_id)
        columns = list(kwargs.keys())
        columns = [column + " = ?" for column in columns]
        columns = " , ".join(columns)
        try:
            self.sql = f"UPDATE VEHICLES SET {columns} WHERE vehicle_id = ?"
            self.cursor.execute(self.sql, (values))
            self.connection.commit()
        except sqlite3.IntegrityError:
            raise sqlite3.IntegrityError()
        except Exception:
            raise VehicleUpdateException()

    def delete(self, vehicle_id:int):
        """Delete a vehicle."""
        self.sql = "SELECT * FROM REPAIRS WHERE vehicle_id=?"
        values = self.cursor.execute(self.sql, (vehicle_id,))
        response = [value for value in values]
        if response:
            error_message = "The vehicle contains a repair registered."
            raise VehicleDeleteException(message=error_message)
        try:
            self.sql = "DELETE FROM VEHICLES WHERE vehicle_id=?"
            self.cursor.execute(self.sql, (vehicle_id,))
            self.connection.commit()
        except Exception:
            raise VehicleDeleteException()

    def drop_table(self):
        """Drop table vehicle."""
        self.sql = "DROP TABLE VEHICLES"
        self.cursor.execute(self.sql)
        self.connection.commit()
