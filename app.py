import datetime

from settings import DATABASE
from core.client import Client
from core.vehicle_type import VehicleType
from core.vehicle import Vehicle
from core.repair import Repair
from database.database import Database
from database.schema import CLIENTS
from database.schema import VEHICLES_TYPE
from database.schema import VEHICLES
from database.schema import REPAIRS

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
    "phone": "0251-48244935",
    "address": "yaritagua"
}
client.create(data=client_data)
print(client.get_all())



vehicle_type = VehicleType(connection=connection)
vehicle_type_data = {
    "brand": "chevrolet",
    "model": "aveo",
    "year": 2007
}

vehicle_type.create(data=vehicle_type_data)
print(vehicle_type.get_all())



vehicle = Vehicle(connection=connection)
vehicle_data = {
    "client_id": 1,
    "vehicle_type_id": 1,
    "identity": "FY-IYHY",
    "mileage": 125.33
}
vehicle.create(data=vehicle_data)
print(vehicle.get_all())
print(vehicle.get_vehicles_with_type_details())
print(vehicle.get_vehicles_with_clients_details())

vehicle_data_2 = {
    "client_id": 1,
    "vehicle_type_id": 1,
    "identity": "AAA",
    "mileage": 1500
}
print(vehicle.update(vehicle_id=1, data=vehicle_data_2))
print(vehicle.get_all())

repair = Repair(connection=connection)
repair_data = {
    "vehicle_id": 1,
    "client_id": 1,
    "diagnostic": "Posible cortocircuito en el motor.",
    "date_entry": datetime.date.today(),
    "date_exit": "",
    "final_observations": "Solucion del cortocircuito, se requiere chequeo cada 6 meses.",
    "price": 10000
}
print(repair.create(data=repair_data))
print(repair.get_repairs_with_vehicles_and_clients_details())
print(repair.get_all())
