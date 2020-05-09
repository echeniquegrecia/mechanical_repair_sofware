from graphic_interface.menus.home.menu_home import MenuHome
import tkinter as tk

from settings import DATABASE
from backend.database.database import Database
from backend.database.schema import CLIENTS
from backend.database.schema import VEHICLES_TYPE
from backend.database.schema import VEHICLES
from backend.database.schema import REPAIRS

database = Database(database=DATABASE)
connection = database.get_connection()

# Create tables
# table_clients = database.create_table(CLIENTS)
# table_vehicles_type = database.create_table(VEHICLES_TYPE)
# table_vehicles = database.create_table(VEHICLES)
# table_repairs = database.create_table(REPAIRS)

root = tk.Tk()
window_principal = MenuHome(root= root, connection=connection)
