from graphic_interface.menus.window_principal import WindowPrincipal
import tkinter as tk

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

root = tk.Tk()
window_principal = WindowPrincipal(root= root, connection=connection)