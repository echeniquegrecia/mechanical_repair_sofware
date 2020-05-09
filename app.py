import datetime

from settings import DATABASE
from backend.core.client import Client
from backend.core.vehicle_type import VehicleType
from backend.core.vehicle import Vehicle
from backend.core.repair import Repair
from backend.database.database import Database
from backend.database.schema import CLIENTS
from backend.database.schema import VEHICLES_TYPE
from backend.database.schema import VEHICLES
from backend.database.schema import REPAIRS

database = Database(database=DATABASE)
connection = database.get_connection()

# Create tables
table_clients = database.create_table(CLIENTS)
table_vehicles_type = database.create_table(VEHICLES_TYPE)
table_vehicles = database.create_table(VEHICLES)
table_repairs = database.create_table(REPAIRS)



client = Client(connection=connection)
client_data= {
    "name": "grecia",
    "last_name": "echenique",
    "identity_card": "19265565",
    "email": "grecia@gmail.com",
    "phone_1": "0251-48244935",
    "phone_2": "0414-2549632",
    "address": "yaritagua"
}

client.create(data=client_data)
# client.create(data=client_data_2)
# client.create(data=client_data_3)
print(client.get_all())
# print(client.get_by_identity_card(identity_card="7547162"))


vehicle_type = VehicleType(connection=connection)
vehicle_type_data = {
    "brand": "chevrolet",
    "model": "aveo",
    "year": 2007
}

vehicle_type.create(data=vehicle_type_data)
# vehicle_type.create(data=vehicle_type_data_2)
# vehicle_type.create(data=vehicle_type_data_3)
print(vehicle_type.get_all())



vehicle = Vehicle(connection=connection)
vehicle_data = {
    "client_id": 1,
    "vehicle_type_id": 1,
    "identity": "FY-IYHY",
    "color": "azul"
}

vehicle.create(data=vehicle_data)
# vehicle.create(data=vehicle_data_2)
# vehicle.create(data=vehicle_data_3)
print(vehicle.get_all())
# print(vehicle.get_vehicles_with_type_details())
# print(vehicle.get_vehicles_with_clients_details())



repair = Repair(connection=connection)
repair_data = {
    "vehicle_id": 1,
    "client_id": 1,
    "mileage": 28512.25,
    "client_observations": "Ruido en la caja",
    "mechanical_observations": "Cortocircuito en el motor",
    "date_entry": str(datetime.date.today()),
    "date_exit": "",
    "other_observations": "Se requiere chequeo cada 6 meses.",
    "price": 10000,
    "repair_status": 1
}
print(repair.create(data=repair_data))
# print(repair.create(data=repair_data_2))
# print(repair.create(data=repair_data_3))
# print(repair.get_all_repairs_with_details())
print(repair.get_all())
# print(repair.get_by_status(repair_status=0))
# print(repair.get_by_status(repair_status=1))
# print(repair.get_by_date_entry(date_entry="2020-03-01"))
# print(repair.get_all())
# print(repair.get_repairs_by_date_entry_with_details(date_entry="2020-03-01"))
# print(repair.get_repairs_by_date_exit_with_details(date_exit="2020-03-15"))
# print(repair.get_repairs_by_date_exit_with_details(date_exit=""))
# print(repair.get_repairs_by_status_with_details(repair_status=0))
# print(repair.get_all_repairs_with_details())
# print(repair.get_repairs_by_client_last_name_with_details(last_name="hernandez"))
#
