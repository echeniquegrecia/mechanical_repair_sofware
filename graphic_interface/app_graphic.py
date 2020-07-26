import tkinter as tk

from settings import DATABASE
from backend.database.database import Database
from graphic_interface.menus.home.menu_home import MenuHome


def app_graphic():
    """Run app graphic."""
    database = Database(database=DATABASE)
    connection = database.get_connection()
    root = tk.Tk()
    MenuHome(root= root, connection=connection)
