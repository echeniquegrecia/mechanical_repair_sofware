class Vehicle:
    """Class Vehicle."""

    def __init__(self, connection):
        """Vehicle init."""
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.sql = ""

    def get_all(self):
        """Get all vehicles."""
        self.sql = "SELECT * FROM VEHICLES"
        self.cursor.execute(self.sql)
        columns = list(map(lambda x: x[0], self.cursor.description))
        values = list(self.cursor.fetchall())
        vehicles = [dict(zip(columns, value)) for value in values]
        vehicles= vehicles if vehicles else []
        return vehicles

    def get_by_id(self, vehicle_id: int):
        """Get vehicle by vehicle_id."""
        self.sql = "SELECT * FROM VEHICLES WHERE vehicle_id=?"
        columns = list(map(lambda x: x[0], self.cursor.description))
        values = self.cursor.execute(self.sql, (vehicle_id,))
        vehicles = [dict(zip(columns, value)) for value in values]
        vehicle = vehicles[0] if vehicles else {}
        return vehicle

    def get_by_client_id(self, client_id: int):
        """Get vehicle by client id."""
        self.sql = "SELECT * FROM VEHICLES WHERE client_id=?"
        columns = list(map(lambda x: x[0], self.cursor.description))
        values = self.cursor.execute(self.sql, (client_id,))
        vehicles = [dict(zip(columns, value)) for value in values]
        vehicle = vehicles[0] if vehicles else {}
        return vehicle

    def get_by_vehicle_type_id(self, vehicle_type_id: int):
        """Get vehicle by vehicle type id."""
        self.sql = "SELECT * FROM VEHICLES WHERE vehicle_type_id=?"
        columns = list(map(lambda x: x[0], self.cursor.description))
        values = self.cursor.execute(self.sql, (vehicle_type_id,))
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_by_identity(self, identity: int):
        """Get vehicle by identity."""
        self.sql = "SELECT * FROM VEHICLES WHERE identity=?"
        columns = list(map(lambda x: x[0], self.cursor.description))
        values = self.cursor.execute(self.sql, (identity,))
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_by_mileage(self, mileage: int):
        """Get vehicle by mileage."""
        self.sql = "SELECT * FROM VEHICLES WHERE mileage=?"
        columns = list(map(lambda x: x[0], self.cursor.description))
        values = self.cursor.execute(self.sql, (mileage,))
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_vehicles_with_type_details(self):
        """Get vehicles with type details."""
        self.sql = "" \
        "SELECT VEHICLES.vehicle_id," \
                "identity," \
                "mileage,"  \
                "brand," \
                "model," \
                "year " \
        "FROM VEHICLES "\
        "INNER JOIN VEHICLES_TYPE ON VEHICLES_TYPE.vehicle_type_id = VEHICLES.vehicle_type_id;"
        self.cursor.execute(self.sql)
        columns = ["vehicle_id", "identity", "mileage", "brand", "model", "year"]
        values = list(self.cursor.fetchall())
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_vehicles_with_clients_details(self):
        """Get vehicles with clients details."""
        self.sql = "" \
        "SELECT VEHICLES.vehicle_id ," \
                "VEHICLES.identity AS vehicle_identity," \
                "VEHICLES.mileage AS mileage," \
                "VEHICLES_TYPE.model AS model," \
                "VEHICLES_TYPE.brand AS brand," \
                "VEHICLES_TYPE.year AS year," \
                "CLIENTS.name as client_name," \
                "CLIENTS.last_name as client_last_name," \
                "CLIENTS.identity_card as client_identity " \
                "FROM VEHICLES_TYPE " \
        "INNER JOIN VEHICLES ON VEHICLES.vehicle_type_id = VEHICLES_TYPE.vehicle_type_id " \
        "INNER JOIN CLIENTS ON CLIENTS.client_id = VEHICLES.client_id;"
        self.cursor.execute(self.sql)
        columns = [
            "vehicle_id",
            "vehicle_identity",
            "mileage",
            "model",
            "brand",
            "year",
            "client_name",
            "client_last_name",
            "client_identity"
        ]
        values = list(self.cursor.fetchall())
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_vehicles_by_item(self, item: str, value):
        """Get vehicles by an item specific with client details."""
        self.sql = "" \
                   "SELECT VEHICLES.vehicle_id ," \
                   "VEHICLES.identity AS vehicle_identity," \
                   "VEHICLES.mileage AS mileage," \
                   "VEHICLES_TYPE.model AS model," \
                   "VEHICLES_TYPE.brand AS brand," \
                   "VEHICLES_TYPE.year AS year," \
                   "CLIENTS.name as client_name," \
                   "CLIENTS.last_name as client_last_name," \
                   "CLIENTS.identity_card as client_identity " \
                   "FROM VEHICLES_TYPE " \
                   "INNER JOIN VEHICLES ON VEHICLES.vehicle_type_id = VEHICLES_TYPE.vehicle_type_id " \
                   "INNER JOIN CLIENTS ON CLIENTS.client_id = VEHICLES.client_id " \
                   f"WHERE {item} =?;"
        self.cursor.execute(self.sql, (value,))
        columns = [
            "vehicle_id",
            "vehicle_identity",
            "mileage",
            "model",
            "brand",
            "year",
            "client_name",
            "client_last_name",
            "client_identity"
        ]
        values = list(self.cursor.fetchall())
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def create(self, data:dict):
        """Create a vehicle."""
        columns = ",".join([*data.keys()])
        values = list(data.values())
        placeholders = ','.join(['?'] * len(data))
        try:
            self.sql = f"INSERT INTO VEHICLES({columns}) VALUES({placeholders})"
            self.cursor.execute(self.sql, values)
            self.connection.commit()
            result = True
        except Exception:
            result = False
        return result

    def update(self, vehicle_id: int, data:dict):
        """Update vehicle details."""
        values = list(data.values())
        values.append(vehicle_id)
        columns = list(data.keys())
        columns = [column + " = ?" for column in columns]
        columns = " , ".join(columns)
        try:
            self.sql = f"UPDATE VEHICLES SET {columns} WHERE vehicle_id = ?"
            self.cursor.execute(self.sql, (values))
            self.connection.commit()
            result = True
        except Exception:
            result = False
        return result

    def delete(self, vehicle_id:int):
        """Delete a vehicle."""
        try:
            self.sql = "DELETE FROM VEHICLES WHERE vehicle_id=?"
            self.cursor.execute(self.sql, (vehicle_id,))
            self.connection.commit()
            result = True
        except Exception:
            result = False
        return result
