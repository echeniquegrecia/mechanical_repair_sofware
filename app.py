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
    "phone_1": "0251-48244935",
    "phone_2": "0414-2549632",
    "address": "yaritagua"
}
client_data_2= {
    "name": "luis",
    "last_name": "hernandez",
    "identity_card": "7547162",
    "email": "luis@gmail.com",
    "phone_1": "0255-568741258",
    "phone_2": "0416-9997841",
    "address": "Acarigua"
}
client_data_3= {
    "name": "marta",
    "last_name": "aponte",
    "identity_card": "8741236",
    "email": "marta@gmail.com",
    "phone_1": "0251-33378514",
    "phone_2": "0414-44478326",
    "address": "barquisimeto"
}
client.create(data=client_data)
client.create(data=client_data_2)
client.create(data=client_data_3)
print(client.get_all())
print(client.get_by_identity_card(identity_card="7547162"))


vehicle_type = VehicleType(connection=connection)
vehicle_type_data = {
    "brand": "chevrolet",
    "model": "aveo",
    "year": 2007
}
vehicle_type_data_2= {
    "brand": "chevrolet",
    "model": "tahoma",
    "year": 2013
}

vehicle_type_data_3= {
    "brand": "chevrolet",
    "model": "blazer",
    "year": 1998
}

vehicle_type.create(data=vehicle_type_data)
vehicle_type.create(data=vehicle_type_data_2)
vehicle_type.create(data=vehicle_type_data_3)
print(vehicle_type.get_all())



vehicle = Vehicle(connection=connection)
vehicle_data = {
    "client_id": 1,
    "vehicle_type_id": 1,
    "identity": "FY-IYHY",
    "mileage": 125.33
}
vehicle_data_2 = {
    "client_id": 2,
    "vehicle_type_id": 2,
    "identity": "GGGG",
    "mileage": 1500
}
vehicle_data_3 = {
    "client_id": 3,
    "vehicle_type_id": 3,
    "identity": "AZ-78J",
    "mileage": 750
}
vehicle.create(data=vehicle_data)
vehicle.create(data=vehicle_data_2)
vehicle.create(data=vehicle_data_3)
print(vehicle.get_all())
print(vehicle.get_vehicles_with_type_details())
print(vehicle.get_vehicles_with_clients_details())



repair = Repair(connection=connection)
repair_data = {
    "vehicle_id": 1,
    "client_id": 1,
    "diagnostic": "Posible cortocircuito en el motor.",
    "date_entry": str(datetime.date.today()),
    "date_exit": "",
    "final_observations": "Solucion del cortocircuito, se requiere chequeo cada 6 meses.",
    "price": 10000,
    "repair_status": 1
}
repair_data_2 = {
    "vehicle_id": 2,
    "client_id": 2,
    "diagnostic": "xxx.",
    "date_entry": "2020-02-29",
    "date_exit": "2020-03-15",
    "final_observations": "XXXXX",
    "price": 20,
    "repair_status": 0
}
repair_data_3 = {
    "vehicle_id": 3,
    "client_id": 3,
    "diagnostic": "Cambio de aceite",
    "date_entry": "2020-01-20",
    "date_exit": "2020-01-21",
    "final_observations": "Ninguna",
    "price": 50000,
    "repair_status": 0
}
print(repair.create(data=repair_data))
print(repair.create(data=repair_data_2))
print(repair.create(data=repair_data_3))
print(repair.get_all_repairs_with_details())
print(repair.get_all())
print(repair.get_by_status(repair_status=0))
print(repair.get_by_status(repair_status=1))
print(repair.get_by_date_entry(date_entry="2020-03-01"))
print(repair.get_all())
print(repair.get_repairs_by_date_entry_with_details(date_entry="2020-03-01"))
print(repair.get_repairs_by_date_exit_with_details(date_exit="2020-03-15"))
print(repair.get_repairs_by_date_exit_with_details(date_exit=""))
print(repair.get_repairs_by_status_with_details(repair_status=0))
print(repair.get_all_repairs_with_details())
print(repair.get_repairs_by_client_last_name_with_details(last_name="hernandez"))

