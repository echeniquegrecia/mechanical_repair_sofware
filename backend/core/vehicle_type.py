from backend.exceptions.vehicle_type_exceptions import VehicleTypeUpdateException
from backend.exceptions.vehicle_type_exceptions import VehicleTypeGetAllException
from backend.exceptions.vehicle_type_exceptions import VehicleTypeGetCategoryException
from backend.exceptions.vehicle_type_exceptions import VehicleTypeFormatDataException
from backend.exceptions.vehicle_type_exceptions import VehicleTypeCreateException
from backend.exceptions.vehicle_type_exceptions import VehicleTypeDeleteException
from backend.service.check_vehicle_type_data import CheckVehicleTypeDataFormat
from backend.service.convert_uppercase import convert_uppercase


class VehicleType:
    """Class Vehicle Type."""

    def __init__(self, connection):
        """VehicleType init."""
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.sql = ""

    def get_all(self):
        """Get all vehicles type."""
        try:
            self.sql = "SELECT * FROM VEHICLES_TYPE"
            self.cursor.execute(self.sql)
            values = list(self.cursor.fetchall())
        except Exception:
            raise VehicleTypeGetAllException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicles_types = [dict(zip(columns, value)) for value in values]
        return vehicles_types

    def get_by_id(self, vehicle_type_id: int):
        """Get vehicle type by vehicle_type_id."""
        try:
            self.sql = "SELECT * FROM VEHICLES_TYPE WHERE vehicle_type_id=?"
            values = self.cursor.execute(self.sql, (vehicle_type_id,))
        except Exception:
            raise VehicleTypeGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicles_type = [dict(zip(columns, value)) for value in values]
        return vehicles_type

    def get_by_brand(self, brand: str):
        """Get vehicle type by brand."""
        try:
            self.sql = "SELECT * FROM VEHICLES_TYPE WHERE brand=?"
            values = self.cursor.execute(self.sql, (brand,))
        except Exception:
            raise VehicleTypeGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicle_types = [dict(zip(columns, value)) for value in values]
        return vehicle_types

    def get_by_model(self, model: str):
        """Get vehicle type by model."""
        try:
            self.sql = "SELECT * FROM VEHICLES_TYPE WHERE model=?"
            values = self.cursor.execute(self.sql, (model,))
        except Exception:
            raise VehicleTypeGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicle_types = [dict(zip(columns, value)) for value in values]
        return vehicle_types

    def get_by_year(self, year: int):
        """Get vehicle type by year."""
        try:
            self.sql = "SELECT * FROM VEHICLES_TYPE WHERE year=?"
            values = self.cursor.execute(self.sql, (year,))
        except Exception:
            raise VehicleTypeGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicle_types = [dict(zip(columns, value)) for value in values]
        return vehicle_types

    def get_vehicle_type_id(self, brand: str, model: str, year: int):
        """Get vehicle type id by the brand, model and year."""
        vehicle_type_id = None
        vehicle_types = self.get_all()
        for vehicle_type in vehicle_types:
            if vehicle_type.get("brand") == brand:
                if vehicle_type.get("model") == model:
                    if vehicle_type.get("year") == year:
                        vehicle_type_id = vehicle_type.get("vehicle_type_id")
        return vehicle_type_id

    def create(self, **kwargs):
        """Create a vehicle type

         **kwargs:
        brand: vehicle brand
        model: vehicle model
        year: vehicle year.
        """

        try:
            CheckVehicleTypeDataFormat(vehicle_type_data=kwargs)
        except VehicleTypeFormatDataException as error:
            raise VehicleTypeFormatDataException(message=error.message)
        kwargs = convert_uppercase(param=kwargs)
        columns = ",".join([*kwargs.keys()])
        values = list(kwargs.values())
        placeholders = ','.join(['?'] * len(kwargs))
        try:
            self.sql = f"INSERT INTO VEHICLES_TYPE({columns}) VALUES({placeholders})"
            self.cursor.execute(self.sql, values)
            self.connection.commit()
        except Exception:
            raise VehicleTypeCreateException()

    def update(self, vehicle_type_id: int, **kwargs):
        """Update vehicle type details.

         **kwargs:
        brand: vehicle brand
        model: vehicle model
        year: vehicle year.
        """

        try:
            CheckVehicleTypeDataFormat(vehicle_type_data=kwargs)
        except VehicleTypeFormatDataException as error:
            raise VehicleTypeFormatDataException(message=error.message)
        kwargs = convert_uppercase(param=kwargs)
        values = list(kwargs.values())
        values.append(vehicle_type_id)
        columns = list(kwargs.keys())
        columns = [column + " = ?" for column in columns]
        columns = " , ".join(columns)
        try:
            self.sql = f"UPDATE VEHICLES_TYPE SET {columns} WHERE vehicle_type_id = ?"
            self.cursor.execute(self.sql, values)
            self.connection.commit()
        except Exception:
            raise VehicleTypeUpdateException()

    def delete(self, vehicle_type_id: int):
        """Delete a vehicle type."""
        self.sql = "SELECT * FROM VEHICLES WHERE vehicle_type_id=?"
        values = self.cursor.execute(self.sql, (vehicle_type_id,))
        response = [value for value in values]
        if response:
            error_message = "The vehicle type contains a vehicle registered."
            raise VehicleTypeDeleteException(message=error_message)
        try:
            self.sql = "DELETE FROM VEHICLES_TYPE WHERE vehicle_type_id=?"
            self.cursor.execute(self.sql, (vehicle_type_id,))
            self.connection.commit()
        except Exception:
            raise VehicleTypeDeleteException()
