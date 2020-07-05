from backend.exceptions.repair_exceptions import RepairDeleteException
from backend.exceptions.repair_exceptions import RepairUpdateException
from backend.exceptions.repair_exceptions import RepairCreateException
from backend.exceptions.repair_exceptions import RepairGetAllException
from backend.exceptions.repair_exceptions import RepairGetCategoryException
from backend.service.check_repair_data import CheckRepairDataFormat
from backend.service.convert_uppercase import convert_uppercase


class Repair:
    """Class Repair."""

    def __init__(self, connection):
        """Repair init."""
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.sql = ""

    def get_all(self):
        """Get all the repairs."""
        try:
            self.sql = "SELECT * FROM REPAIRS"
            self.cursor.execute(self.sql)
            values = list(self.cursor.fetchall())
        except Exception:
            raise RepairGetAllException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        repairs = [dict(zip(columns, value)) for value in values]
        return repairs

    def get_by_vehicle_id(self, vehicle_id: int):
        """Get repair by vehicle id."""
        try:
            self.sql = "SELECT * FROM REPAIRS WHERE vehicle_id=?"
            values = self.cursor.execute(self.sql, (vehicle_id,))
        except Exception:
            raise RepairGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        repairs = [dict(zip(columns, value)) for value in values]
        return repairs

    def get_by_client_id(self, client_id: int):
        """Get repair by client id."""
        try:
            self.sql = "SELECT * FROM REPAIRS WHERE client_id=?"
            values = self.cursor.execute(self.sql, (client_id,))
        except Exception:
            raise RepairGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        repairs = [dict(zip(columns, value)) for value in values]
        return repairs

    def get_by_date_entry(self, date_entry: str):
        """Get repair by date entry"""
        try:
            self.sql = "SELECT * FROM REPAIRS WHERE date_entry=?"
            values = self.cursor.execute(self.sql, (date_entry,))
        except Exception:
            raise RepairGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        repairs = [dict(zip(columns, value)) for value in values]
        return repairs

    def get_by_date_exit(self, date_exit: str):
        """Get repair by date exit"""
        try:
            self.sql = "SELECT * FROM REPAIRS WHERE date_exit=?"
            values = self.cursor.execute(self.sql, (date_exit,))
        except Exception:
            raise RepairGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        repairs = [dict(zip(columns, value)) for value in values]
        return repairs

    def get_by_status(self, repair_status: str):
        """Get repair by date exit"""
        try:
            self.sql = "SELECT * FROM REPAIRS WHERE repair_status=?"
            values = self.cursor.execute(self.sql, (repair_status,))
        except Exception:
            raise RepairGetCategoryException()
        columns = list(map(lambda x: x[0], self.cursor.description))
        repairs = [dict(zip(columns, value)) for value in values]
        return repairs

    def get_all_repairs_with_details(self):
        """Get repairs with vehicles and clients details."""
        try:
            self.sql = "" \
                "SELECT REPAIRS.repair_id, " \
                       "REPAIRS.status, " \
                       "REPAIRS.mileage, " \
                       "VEHICLES.identity, " \
                       "VEHICLES_TYPE.brand, " \
                       "VEHICLES_TYPE.model, " \
                       "VEHICLES_TYPE.year, " \
                       "REPAIRS.date_entry, " \
                       "REPAIRS.date_exit, " \
                       "CLIENTS.name," \
                       "CLIENTS.last_name," \
                       "CLIENTS.identity_card " \
                "FROM REPAIRS " \
                "INNER JOIN VEHICLES USING(vehicle_id) " \
                "INNER JOIN VEHICLES_TYPE USING(vehicle_type_id) " \
                "INNER JOIN CLIENTS USING(client_id) "
            self.cursor.execute(self.sql)
            columns = [
                "repair_id",
                "status",
                "mileage",
                "identity",
                "brand",
                "model",
                "year",
                "date_entry",
                "date_exit",
                "client_name",
                "client_last_name",
                "client_identity"
            ]
            values = list(self.cursor.fetchall())
        except Exception:
            raise RepairGetCategoryException()
        repairs = [dict(zip(columns, value)) for value in values]
        return repairs

    def get_repairs_by_category(self, category: str, value):
        """Get repairs with vehicles and clients details."""
        try:
            self.sql = "" \
                "SELECT REPAIRS.repair_id, " \
                       "REPAIRS.status, " \
                       "REPAIRS.mileage, " \
                       "VEHICLES.identity, " \
                       "VEHICLES_TYPE.brand, " \
                       "VEHICLES_TYPE.model, " \
                       "VEHICLES_TYPE.year, " \
                       "REPAIRS.date_entry, " \
                       "REPAIRS.date_exit, " \
                       "CLIENTS.name," \
                       "CLIENTS.last_name," \
                       "CLIENTS.identity_card " \
                "FROM REPAIRS " \
                "INNER JOIN VEHICLES USING(vehicle_id) " \
                "INNER JOIN VEHICLES_TYPE USING(vehicle_type_id) " \
                "INNER JOIN CLIENTS USING(client_id) " \
                f"WHERE {category} =?;"
            self.cursor.execute(self.sql, (value,))
            columns = [
                "repair_id",
                "status",
                "mileage",
                "identity",
                "brand",
                "model",
                "year",
                "date_entry",
                "date_exit",
                "client_name",
                "client_last_name",
                "client_identity"
            ]
            values = list(self.cursor.fetchall())
        except Exception:
            raise RepairGetCategoryException()
        repairs = [dict(zip(columns, value)) for value in values]
        return repairs

    def get_repairs_by_date_entry_with_details(self, date_entry: str):
        """Get repairs with vehicles and clients details by model."""
        try:
            self.sql = "" \
                "SELECT REPAIRS.repair_id," \
                       "VEHICLES.identity," \
                       "VEHICLES_TYPE.brand," \
                       "VEHICLES_TYPE.model," \
                       "VEHICLES_TYPE.year," \
                       "REPAIRS.date_entry," \
                       "REPAIRS.date_exit," \
                       "CLIENTS.name," \
                       "CLIENTS.last_name," \
                       "CLIENTS.identity_card " \
                "FROM REPAIRS " \
                "INNER JOIN VEHICLES ON VEHICLES.vehicle_id = REPAIRS.vehicle_id " \
                "INNER JOIN VEHICLES_TYPE ON VEHICLES_TYPE.vehicle_type_id = VEHICLES.vehicle_id " \
                "INNER JOIN CLIENTS ON CLIENTS.client_id = VEHICLES.client_id " \
                f"WHERE REPAIRS.date_entry = ?;"
            self.cursor.execute(self.sql, (date_entry,))
            columns = [
                "repair_id",
                "identity",
                "brand",
                "model",
                "year",
                "date_entry",
                "date_exit",
                "client_name",
                "client_last_name",
                "client_identity"
            ]
            values = list(self.cursor.fetchall())
        except Exception:
            raise RepairGetCategoryException()
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_repairs_by_date_exit_with_details(self, date_exit: str):
        """Get repairs with vehicles and clients details by model."""
        try:
            self.sql = "" \
                "SELECT REPAIRS.repair_id," \
                       "VEHICLES.identity," \
                       "VEHICLES_TYPE.brand," \
                       "VEHICLES_TYPE.model," \
                       "VEHICLES_TYPE.year," \
                       "REPAIRS.date_entry," \
                       "REPAIRS.date_exit," \
                       "CLIENTS.name," \
                       "CLIENTS.last_name," \
                       "CLIENTS.identity_card " \
                "FROM REPAIRS " \
                "INNER JOIN VEHICLES ON VEHICLES.vehicle_id = REPAIRS.vehicle_id " \
                "INNER JOIN VEHICLES_TYPE ON VEHICLES_TYPE.vehicle_type_id = VEHICLES.vehicle_id " \
                "INNER JOIN CLIENTS ON CLIENTS.client_id = VEHICLES.client_id " \
                f"WHERE REPAIRS.date_exit = ?;"
            self.cursor.execute(self.sql, (date_exit,))
            columns = [
                "repair_id",
                "identity",
                "brand",
                "model",
                "year",
                "date_entry",
                "date_exit",
                "client_name",
                "client_last_name",
                "client_identity"
            ]
            values = list(self.cursor.fetchall())
        except Exception:
            raise RepairGetCategoryException()
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_repairs_by_status_with_details(self, repair_status: str):
        """Get repairs with vehicles and clients details by model."""
        try:
            self.sql = "" \
                "SELECT REPAIRS.repair_id," \
                       "VEHICLES.identity," \
                       "VEHICLES_TYPE.brand," \
                       "VEHICLES_TYPE.model," \
                       "VEHICLES_TYPE.year," \
                       "REPAIRS.date_entry," \
                       "REPAIRS.date_exit," \
                       "CLIENTS.name," \
                       "CLIENTS.last_name," \
                       "CLIENTS.identity_card " \
                "FROM REPAIRS " \
                "INNER JOIN VEHICLES ON VEHICLES.vehicle_id = REPAIRS.vehicle_id " \
                "INNER JOIN VEHICLES_TYPE ON VEHICLES_TYPE.vehicle_type_id = VEHICLES.vehicle_id " \
                "INNER JOIN CLIENTS ON CLIENTS.client_id = VEHICLES.client_id " \
                f"WHERE REPAIRS.repair_status = ?;"
            self.cursor.execute(self.sql, (repair_status,))
            columns = [
                "repair_id",
                "identity",
                "brand",
                "model",
                "year",
                "date_entry",
                "date_exit",
                "client_name",
                "client_last_name",
                "client_identity"
            ]
            values = list(self.cursor.fetchall())
        except Exception:
            raise RepairGetCategoryException()
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def get_by_id(self, repair_id):
        """Get repair by id."""
        try:
            self.sql = "" \
                "SELECT REPAIRS.repair_id," \
                       "REPAIRS.mileage," \
                       "REPAIRS.client_observations," \
                       "REPAIRS.mechanical_observations," \
                       "REPAIRS.final_observations," \
                       "REPAIRS.date_entry," \
                       "REPAIRS.date_exit," \
                       "REPAIRS.price," \
                       "REPAIRS.status," \
                       "VEHICLES.vehicle_id," \
                       "VEHICLES.identity," \
                       "VEHICLES.color," \
                       "VEHICLES_TYPE.vehicle_type_id," \
                       "VEHICLES_TYPE.brand," \
                       "VEHICLES_TYPE.model," \
                       "VEHICLES_TYPE.year," \
                       "CLIENTS.client_id," \
                       "CLIENTS.name," \
                       "CLIENTS.last_name," \
                       "CLIENTS.identity_card," \
                       "CLIENTS.email," \
                       "CLIENTS.phone_1," \
                       "CLIENTS.phone_2," \
                       "CLIENTS.address " \
                "FROM REPAIRS " \
                "INNER JOIN VEHICLES USING(vehicle_id) " \
                "INNER JOIN VEHICLES_TYPE USING(vehicle_type_id) " \
                "INNER JOIN CLIENTS USING(client_id) " \
                "WHERE REPAIRS.repair_id = ?;"
            self.cursor.execute(self.sql, (repair_id,))
            columns = [
                "repair_id",
                "mileage",
                "client_observations",
                "mechanical_observations",
                "final_observations",
                "date_entry",
                "date_exit",
                "price",
                "status",
                "vehicle_id",
                "vehicle_identity",
                "vehicle_color",
                "vehicle_type_id",
                "vehicle_type_brand",
                "vehicle_type_model",
                "vehicle_type_year",
                "client_id",
                "client_name",
                "client_last_name",
                "client_identity_card",
                "client_email",
                "client_phone_1",
                "client_phone_2",
                "client_address"
            ]
            values = list(self.cursor.fetchall())
        except Exception:
            raise RepairGetCategoryException()
        vehicles = [dict(zip(columns, value)) for value in values]
        return vehicles

    def create(self, **kwargs):
        """Create a repair.

        **kwargs:
        vehicle_id: vehicle id
        mileage: mileage vehicle
        client_observations: observation from clients
        mechanical_observations: observations from mechanical
        final_observations: observations post reparation
        date_entry:
        date_exit:
        price:
        status: "EN TALLER", "FINALIZADO".
        """
        kwargs = convert_uppercase(param=kwargs)
        CheckRepairDataFormat(kwargs)
        columns = ",".join([*kwargs.keys()])
        values = list(kwargs.values())
        placeholders = ','.join(['?'] * len(kwargs))
        try:
            self.sql = f"INSERT INTO REPAIRS({columns}) VALUES({placeholders})"
            self.cursor.execute(self.sql, values)
            self.connection.commit()
        except Exception:
            raise RepairCreateException()

    def update(self, repair_id: int, **kwargs):
        """Update repair details.

        **kwargs:
        vehicle_id: vehicle id
        mileage: mileage vehicle
        client_observations: observation from clients
        mechanical_observations: observations from mechanical
        final_observations: observations post reparation
        date_entry:
        date_exit:
        price:
        status: "EN TALLER", "FINALIZADO".
        """
        kwargs = convert_uppercase(param=kwargs)
        CheckRepairDataFormat(kwargs)
        values = list(kwargs.values())
        values.append(repair_id)
        columns = list(kwargs.keys())
        columns = [column + " = ?" for column in columns]
        columns = " , ".join(columns)
        try:
            self.sql = f"UPDATE REPAIRS SET {columns} WHERE repair_id = ?"
            self.cursor.execute(self.sql, (values))
            self.connection.commit()
        except Exception:
            raise RepairUpdateException()

    def delete(self, repair_id: int):
        """Delete a repair."""
        try:
            self.sql = "DELETE FROM REPAIRS WHERE repair_id=?"
            self.cursor.execute(self.sql, (repair_id,))
            self.connection.commit()
        except Exception:
            raise RepairDeleteException()
