import tkinter as tk
from tkinter import filedialog
import pandas as pd
from PIL import Image, ImageTk

from graphic_interface.menus.base_frame import BaseFrame
from graphic_interface.menus.client.menu_client import MenuClient
from graphic_interface.menus.repair.menu_repair import MenuRepair
from graphic_interface.menus.vehicle.menu_vehicle import MenuVehicle
from graphic_interface.menus.vehicle_type.menu_vehicle_type import MenuVehicleType
from settings import IMAGE_MENU


class MenuHome(BaseFrame):
    """Class for MenuHome."""

    def __init__(self, root, connection):
        """MenuHome init."""
        super().__init__(root=root, connection=connection)
        self.root.state('zoomed')

        frame_1 = tk.LabelFrame(self.root, text="Menu", width=100, height=10)
        frame_1.pack(side='left', ipadx=100, padx=5, pady=5, fill='y')

        frame_2 = tk.LabelFrame(self.root, width=300)
        frame_2.pack(side='right', ipadx=320, padx=5, pady=11, fill='both')

        button_1 = tk.Button(frame_1, text="Clientes", font='Helvetica 20 bold', command=self.menu_client)
        button_1.pack(fill='both', pady=10, padx=10)

        button_2 = tk.Button(frame_1, text="Vehiculos", font='Helvetica 20 bold', command=self.menu_vehicle)
        button_2.pack(fill='both', pady=10, padx=10)

        button_3 = tk.Button(frame_1, text="Tipo de Vehiculos", font='Helvetica 20 bold', command=self.menu_vehicle_type)
        button_3.pack(fill='both', pady=10, padx=10)

        button_4 = tk.Button(frame_1, text="Reparaciones", font='Helvetica 20 bold', command=self.menu_repair)
        button_4.pack(fill='both', pady=10, padx=10)

        button_6 = tk.Button(frame_1, text="Exportar datos", font='Helvetica 20 bold', command=self.export_data)
        button_6.pack(fill='both', pady=10, padx=10)

        button_7 = tk.Button(frame_1, text="Importar datos", font='Helvetica 20 bold', command=self.import_data)
        button_7.pack(fill='both', pady=10, padx=10)

        frame_3 = tk.Frame(frame_1, height=100)
        frame_3.pack(fill='both', pady=10, padx=10, expand=True)

        frame_4 = tk.Frame(frame_3)
        frame_4.pack(side='bottom', fill='x')

        button_5 = tk.Button(frame_4, text="Salir", font='Helvetica 15 bold', width=15)
        button_5.pack(side='right', fil='x')

        button_5 = tk.Button(frame_4, text="Reset", font='Helvetica 15 bold', width=15)
        button_5.pack(side='left', fil='x')

        image = Image.open(IMAGE_MENU)
        image = image.resize((950, 800), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        label = tk.Label(frame_2, image=image)
        label.pack(side='right', fill='both', expand=True)

        self.root.mainloop()

    def menu_client(self):
        """Open menu client."""
        self.hide()
        self.new_window = tk.Toplevel(self.root)
        self.app = MenuClient(root=self.new_window, connection=self.connection, master=self)

    def menu_vehicle(self):
        """Open menu vehicle."""
        self.hide()
        self.new_window = tk.Toplevel(self.root)
        self.app = MenuVehicle(root=self.new_window, connection=self.connection, master=self)

    def menu_vehicle_type(self):
        """Open menu vehicle type."""
        self.hide()
        self.new_window = tk.Toplevel(self.root)
        self.app = MenuVehicleType(root=self.new_window, connection=self.connection, master=self)

    def menu_repair(self):
        """Open menu repair."""
        self.hide()
        self.new_window = tk.Toplevel(self.root)
        self.app = MenuRepair(root=self.new_window, connection=self.connection, master=self)

    def export_data(self):
        """Export data."""
        clients_data = self.client.get_all()
        vehicle_types_data = self.vehicle_type.get_all()
        vehicles_data = self.vehicle.get_all()
        repairs_data = self.repair.get_all()

        clients = pd.DataFrame.from_dict(clients_data)
        vehicle_types = pd.DataFrame.from_dict(vehicle_types_data)
        vehicles = pd.DataFrame.from_dict(vehicles_data)
        repairs = pd.DataFrame.from_dict(repairs_data)

        saving_path = filedialog.asksaveasfile(mode="w", defaultextension=".xlsx")

        writer = pd.ExcelWriter(saving_path.name, engine='xlsxwriter')

        clients.to_excel(writer, sheet_name='Clientes')
        vehicle_types.to_excel(writer, sheet_name='Tipos de Vehiculo')
        vehicles.to_excel(writer, sheet_name='Vehiculos')
        repairs.to_excel(writer, sheet_name='Reparaciones')

        writer.save()

    def import_data(self):
        """Import data."""
        file_path = filedialog.askopenfilename()
        clients = pd.read_excel(
            file_path,
            sheet_name='Clientes',
            header=0)

        vehicle_types = pd.read_excel(
            file_path,
            sheet_name='Tipos de Vehiculo',
            header=0)

        vehicles = pd.read_excel(
            file_path,
            sheet_name='Vehiculos',
            header=0)

        repairs = pd.read_excel(
            file_path,
            sheet_name='Reparaciones',
            header=0)

        clients.to_sql('CLIENTS', self.connection, if_exists='append', index=False)
        vehicle_types.to_sql('VEHICLES_TYPE', self.connection, if_exists='append', index=False)
        vehicles.to_sql('VEHICLES', self.connection, if_exists='append', index=False)
        repairs.to_sql('REPAIRS', self.connection, if_exists='append', index=False)
