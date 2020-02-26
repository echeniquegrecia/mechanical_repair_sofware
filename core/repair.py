class Repair:
    """Class Repair."""

    def __init__(self, connection):
        """Repair init."""
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.sql = ""

    def get_all(self):
        """Get all the repairs."""
        self.sql = "SELECT * FROM REPAIRS"
        self.cursor.execute(self.sql)
        columns = list(map(lambda x: x[0], self.cursor.description))
        values = list(self.cursor.fetchall())
        repairs = [dict(zip(columns, value)) for value in values]
        repairs = repairs if repairs else []
        return repairs

    def get_by_id(self, repair_id: int):
        """Get repair by repair_id."""
        self.sql = "SELECT * FROM REPAIRS WHERE repair_id=?"
        columns = list(map(lambda x: x[0], self.cursor.description))
        values = self.cursor.execute(self.sql, (repair_id,))
        repairs = [dict(zip(columns, value)) for value in values]
        repair = repairs[0] if repairs else {}
        return repair

    def get_by_vehicle_id(self, vehicle_id: int):
        """Get repair by vehicle id."""
        self.sql = "SELECT * FROM REPAIRS WHERE vehicle_id=?"
        columns = list(map(lambda x: x[0], self.cursor.description))
        values = self.cursor.execute(self.sql, (vehicle_id,))
        repairs = [dict(zip(columns, value)) for value in values]
        repair = repairs[0] if repairs else {}
        return repair

    def get_by_client_id(self, client_id: int):
        """Get repair by client id."""
        self.sql = "SELECT * FROM REPAIRS WHERE client_id=?"
        columns = list(map(lambda x: x[0], self.cursor.description))
        values = self.cursor.execute(self.sql, (client_id,))
        repairs = [dict(zip(columns, value)) for value in values]
        repair = repairs[0] if repairs else {}
        return repair

    def get_by_date_entry(self, date_entry):
        """Get repair by date entry"""
        self.sql = "SELECT * FROM REPAIRS WHERE date_entry=?"
        columns = list(map(lambda x: x[0], self.cursor.description))
        values = self.cursor.execute(self.sql, (date_entry,))
        repairs = [dict(zip(columns, value)) for value in values]
        repair = repairs[0] if repairs else {}
        return repair

    def get_by_date_exit(self, date_exit):
        """Get repair by date exit"""
        self.sql = "SELECT * FROM REPAIRS WHERE date_exit=?"
        columns = list(map(lambda x: x[0], self.cursor.description))
        values = self.cursor.execute(self.sql, (date_exit,))
        repairs = [dict(zip(columns, value)) for value in values]
        repair = repairs[0] if repairs else {}
        return repair

    def get_repairs_with_vehicles_and_clients_details(self):
        """Get repairs with vehicles and clients details."""
        self.sql = "" \
        "SELECT REPAIRS.repair_id ," \
                "VEHICLES_TYPE.brand AS brand," \
                "VEHICLES_TYPE.model AS model," \
                "VEHICLES_TYPE.year AS year," \
                "REPAIRS.date_entry," \
                "REPAIRS.date_exit," \
                "CLIENTS.name as client_name," \
                "CLIENTS.last_name as client_last_name," \
                "CLIENTS.identity_card as client_identity " \
                "FROM REPAIRS " \
        "INNER JOIN VEHICLES ON VEHICLES.vehicle_id = REPAIRS.vehicle_id " \
        "INNER JOIN VEHICLES_TYPE ON VEHICLES_TYPE.vehicle_type_id = VEHICLES.vehicle_id " \
        "INNER JOIN CLIENTS ON CLIENTS.client_id = VEHICLES.client_id;"
        self.cursor.execute(self.sql)
        columns = [
            "repair_id",
            "brand",
            "model",
            "year",
            "data_entry",
            "data_exit",
            "client_name",
            "client_last_name",
            "client_identity"
        ]
        values = list(self.cursor.fetchall())
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def create(self, data:dict):
        """Create a repair."""
        columns = ",".join([*data.keys()])
        values = list(data.values())
        placeholders = ','.join(['?'] * len(data))
        try:
            self.sql = f"INSERT INTO REPAIRS({columns}) VALUES({placeholders})"
            print(self.sql)
            self.cursor.execute(self.sql, values)
            self.connection.commit()
            result = True
        except Exception:
            result = False
        return result

    def update(self, repair_id: int, data:dict):
        """Update repair details."""
        values = list(data.values())
        values.append(repair_id)
        columns = list(data.keys())
        columns = [column + " = ?" for column in columns]
        columns = " , ".join(columns)
        try:
            self.sql = f"UPDATE REPAIRS SET {columns} WHERE repair_id = ?"
            self.cursor.execute(self.sql, (values))
            self.connection.commit()
            result = True
        except Exception:
            result = False
        return result

    def delete(self, repair_id:int):
        """Delete a repair."""
        try:
            self.sql = "DELETE FROM REPAIRS WHERE repair_id=?"
            self.cursor.execute(self.sql, (repair_id,))
            self.connection.commit()
            result = True
        except Exception:
            result = False
        return result