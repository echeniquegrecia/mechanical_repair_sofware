class VehicleType:
    """Class Vehicle Type."""

    def __init__(self, connection):
        """VehicleType init."""
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.sql = ""

    def get_all(self):
        """Get all vehicles type."""
        self.sql = "SELECT * FROM VEHICLES_TYPE"
        self.cursor.execute(self.sql)
        columns = list(map(lambda x: x[0], self.cursor.description))
        values = list(self.cursor.fetchall())
        vehicles_type = [dict(zip(columns, value)) for value in values]
        vehicles_type = vehicles_type if vehicles_type else []
        return vehicles_type

    def get_by_id(self, vehicle_type_id:int):
        """Get vehicle type by vehicle_type_id."""
        self.sql = "SELECT * FROM VEHICLES_TYPE WHERE vehicle_type_id=?"
        values = self.cursor.execute(self.sql, (vehicle_type_id,))
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicles_type = [dict(zip(columns, value)) for value in values]
        vehicle_type = vehicles_type[0] if vehicles_type else {}
        return vehicle_type

    def get_by_brand(self, brand:str):
        """Get vehicle type by brand."""
        self.sql = "SELECT * FROM VEHICLES_TYPE WHERE brand=?"
        values = self.cursor.execute(self.sql, (brand,))
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicle_types = [dict(zip(columns, value)) for value in values]
        return vehicle_types

    def get_by_model(self, model:str):
        """Get vehicle type by model."""
        self.sql = "SELECT * FROM VEHICLES_TYPE WHERE model=?"
        values = self.cursor.execute(self.sql, (model,))
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicle_types = [dict(zip(columns, value)) for value in values]
        return vehicle_types

    def get_by_year(self, year:int):
        """Get vehicle type by year."""
        self.sql = "SELECT * FROM VEHICLES_TYPE WHERE year=?"
        values = self.cursor.execute(self.sql, (year,))
        columns = list(map(lambda x: x[0], self.cursor.description))
        vehicle_types = [dict(zip(columns, value)) for value in values]
        return vehicle_types

    def get_vehicle_type_id(self, brand:str, model: str, year:int):
        """Get vehicle type id by the brand, model and year."""
        vehicle_type_id = None
        vehicle_types = self.get_all()
        for vehicle_type in vehicle_types:
            if vehicle_type.get("brand") == brand:
                if vehicle_type.get("model") == model:
                    if vehicle_type.get("year") == year:
                        vehicle_type_id = vehicle_type.get("vehicle_type_id")
        return vehicle_type_id

    def create(self, data:dict):
        """Create a vehicle type."""
        columns = ",".join([*data.keys()])
        values = list(data.values())
        placeholders = ','.join(['?'] * len(data))
        try:
            self.sql = f"INSERT INTO VEHICLES_TYPE({columns}) VALUES({placeholders})"
            self.cursor.execute(self.sql, values)
            self.connection.commit()
            result = True
        except Exception:
            result = False
        return result

    def update(self, vehicle_type_id: int, data:dict):
        """Update vehicle type details."""
        values = list(data.values())
        values.append(vehicle_type_id)
        columns = list(data.keys())
        columns = [column + " = ?" for column in columns]
        columns = " , ".join(columns)
        try:
            self.sql = f"UPDATE VEHICLES_TYPE SET {columns} WHERE vehicle_type_id = ?"
            self.cursor.execute(self.sql, (values))
            self.connection.commit()
            result = True
        except Exception:
            result = False
        return result

    def delete(self, vehicle_type_id:int):
        """Delete a vehicle type."""
        try:
            self.sql = "DELETE FROM VEHICLES_TYPE WHERE vehicle_type_id=?"
            self.cursor.execute(self.sql, (vehicle_type_id,))
            self.connection.commit()
            result = True
        except Exception:
            result = False
        return result