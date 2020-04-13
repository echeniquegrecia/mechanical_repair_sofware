from graphic_interface.menus.home.menu_home import MenuHome
import tkinter as tk

from settings import DATABASE
from backend.core.client import Client
from backend.database.database import Database

database = Database(database=DATABASE)
connection = database.get_connection()
client = Client(connection=connection)

root = tk.Tk()
window_principal = MenuHome(root= root, connection=connection)
