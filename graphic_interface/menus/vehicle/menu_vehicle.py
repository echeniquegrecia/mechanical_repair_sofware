import tkinter as tk
from tkinter import ttk
from graphic_interface.menus.base_frame import BaseFrame
from graphic_interface.menus.vehicle.form_new_vehicle import FormNewVehicle
from graphic_interface.menus.vehicle_type.form_edit_vehicle_type import FormEditVehicleType


class MenuVehicle(BaseFrame):
    """Class for Menu Vehicle Window."""

    def __init__(self, root, connection, master):
        """Menu Vehicle Window init."""
        super().__init__(root=root, connection=connection)
        self.root.state('zoomed')
        self.master = master
        self.option_var = tk.StringVar()
        self.entry_var = tk.StringVar()

        frame_1 = tk.LabelFrame(self.root, text="Menu Vehiculo", width=100, height=10)
        frame_1.pack(side='top', padx=5, pady=5, fill='x')

        frame_2 = tk.LabelFrame(self.root, width=100, height=10)
        frame_2.pack(side='left', ipadx=100, padx=5, pady=5, fill='y')

        frame_3 = tk.LabelFrame(self.root)
        frame_3.pack(side='left', padx=5, pady=5, fill='both', expand=True)

        frame_4 = tk.Frame(frame_2)
        frame_4.pack(side='bottom', fill='x')

        button_1 = tk.Button(frame_2, text="Nuevo", font='Helvetica 20 bold', width=15, command=self.create_new_vehicle)
        button_1.pack(fill='both', pady=10, padx=10)

        button_2 = tk.Button(frame_2, text="Editar", font='Helvetica 20 bold', width=15)
        button_2.pack(fill='both', pady=10, padx=10)

        button_3 = tk.Button(frame_2, text="Borrar", font='Helvetica 20 bold', width=15)
        button_3.pack(fill='both', pady=10, padx=10)

        button_4 = tk.Button(frame_2, text="Actualizar", font='Helvetica 20 bold', command=self.update_table)
        button_4.pack(fill='both', pady=10, padx=10)

        button_5 = tk.Button(frame_4, text="Regresar", font='Helvetica 15 bold', command=self.go_back)
        button_5.pack(side='left', pady=10, padx=10)

        # Define search frame
        self.option_var.set("--Seleccione una busqueda--")
        contents = {"Placa", "Kilometraje", "Modelo", "Marca", "Año", "Nombre", "Apellido", "Cedula"}
        self.options = tk.OptionMenu(frame_1, self.option_var, *contents)
        self.options.config(font=('Helvetica', 15))
        self.options.pack(side='left', pady=10, padx=10, fill='x')
        entry = tk.Entry(frame_1, font="Helvetica 15", textvariable=self.entry_var)
        entry.pack(side='left', pady=10, padx=10, fill='x')

        button_6 = tk.Button(frame_1, text="Buscar", font='Helvetica 15 bold', command=self.search_vehicle_by_category)
        button_6.pack(side='left', pady=10, padx=10, fill='x')

        # Define Heading table
        columns = ("Id", "Placa", "Kilometraje", "Modelo", "Marca", "Año", "Nombre", "Apellido", "Cedula")
        self.treeview = ttk.Treeview(frame_3, height=18, show="headings", columns=columns)
        self.treeview.heading("Id", text="Id")
        self.treeview.heading("Placa", text="Placa")
        self.treeview.heading("Kilometraje", text="Kilometraje")
        self.treeview.heading("Modelo", text="Modelo")
        self.treeview.heading("Marca", text="Marca")
        self.treeview.heading("Año", text="Año")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Apellido", text="Apellido")
        self.treeview.heading("Cedula", text="Cedula")

        # Define Columns table
        self.treeview.column("Id", stretch=0, width=20, anchor='center')
        self.treeview.column("Placa",width=150, anchor='center')
        self.treeview.column("Kilometraje", width=150, anchor='center')
        self.treeview.column("Modelo", width=150, anchor='center')
        self.treeview.column("Marca", width=150, anchor='center')
        self.treeview.column("Año", width=150, anchor='center')
        self.treeview.column("Nombre", width=150, anchor='center')
        self.treeview.column("Apellido", width=150, anchor='center')
        self.treeview.column("Cedula", width=150, anchor='center')

        # Insert Data
        vehicles = self.vehicle.get_vehicles_with_clients_details()
        id = [vehicle.get("vehicle_id") for vehicle in vehicles]
        vehicle_identity = [vehicle.get("vehicle_identity") for vehicle in vehicles]
        mileage = [vehicle.get("mileage") for vehicle in vehicles]
        model = [vehicle.get("model") for vehicle in vehicles]
        brand = [vehicle.get("brand") for vehicle in vehicles]
        year = [vehicle.get("year") for vehicle in vehicles]
        client_name = [vehicle.get("client_name") for vehicle in vehicles]
        client_last_name = [vehicle.get("client_last_name") for vehicle in vehicles]
        client_identity = [vehicle.get("client_identity") for vehicle in vehicles]

        for vehicle in range(0, len(vehicles)):
            self.treeview.insert('', vehicle, values=(
                id[vehicle],
                vehicle_identity[vehicle],
                mileage[vehicle],
                model[vehicle],
                brand[vehicle],
                year[vehicle],
                client_name[vehicle],
                client_last_name[vehicle],
                client_identity[vehicle]
            ))

        # Scrollbar Vertical
        scrollbar_vertical = ttk.Scrollbar(frame_3)
        scrollbar_vertical.configure(command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=scrollbar_vertical.set)

        # Scrollbar Horizontal
        scrollbar_horizontal = ttk.Scrollbar(frame_3, orient="horizontal")
        scrollbar_horizontal.configure(command=self.treeview.xview)
        self.treeview.configure(xscrollcommand=scrollbar_horizontal.set)

        # Scrollbar Position
        scrollbar_vertical.pack(side="right", fill="y")
        scrollbar_horizontal.pack(side="bottom", fill="x")
        self.treeview.pack(side="right", fill='both', expand=True)

        self.root.mainloop()

    def create_new_vehicle(self):
        """Create new vehicle."""
        self.new_window = tk.Toplevel(self.root)
        self.app = FormNewVehicle(
            root=self.new_window,
            connection=self.connection,
            master=self
        )

    def get_entry_value(self):
        """Check the entry value."""
        value = self.entry_var.get()
        item = self.option_var.get()
        try:
            if item == "Kilometraje":
                value = float(self.entry_var.get())
            elif item == "Año":
                value = int(self.entry_var.get())
        except Exception:
            self.show_error(message=f"ERROR: El valor: {value} no corresponde con la categoria: {item}.")
        return value

    def get_vehicle_by_item(self):
        """Get vehicle by item."""
        item = {
            "Placa": "vehicle_identity",
            "Kilometraje": "mileage",
            "Modelo": "model",
            "Marca": "brand",
            "Año": "year",
            "Nombre": "client_name",
            "Apellido": "client_last_name",
            "Cedula": "client_identity",
        }
        item = item.get(self.option_var.get(), "")
        value = self.get_entry_value()
        vehicles = self.vehicle.get_vehicles_by_item(item=item, value=value)
        return vehicles

    def search_vehicle_by_category(self):
        """Search vehicle by category."""
        vehicles = self.get_vehicle_by_item()
        id = [vehicle.get("vehicle_id") for vehicle in vehicles]
        vehicle_identity = [vehicle.get("vehicle_identity") for vehicle in vehicles]
        mileage = [vehicle.get("mileage") for vehicle in vehicles]
        model = [vehicle.get("model") for vehicle in vehicles]
        brand = [vehicle.get("brand") for vehicle in vehicles]
        year = [vehicle.get("year") for vehicle in vehicles]
        client_name = [vehicle.get("client_name") for vehicle in vehicles]
        client_last_name = [vehicle.get("client_last_name") for vehicle in vehicles]
        client_identity = [vehicle.get("client_identity") for vehicle in vehicles]

        for i in self.treeview.get_children():
            self.treeview.delete(i)

        for vehicle in range(0, len(vehicles)):
            self.treeview.insert('', vehicle, values=(
                id[vehicle],
                vehicle_identity[vehicle],
                mileage[vehicle],
                model[vehicle],
                brand[vehicle],
                year[vehicle],
                client_name[vehicle],
                client_last_name[vehicle],
                client_identity[vehicle]
            ))

    def get_values(self):
        """Get values."""
        cur_item = self.treeview.focus()
        item = self.treeview.item(cur_item)
        values = item.get("values", [])
        return values

    def go_back(self):
        """Go back to Menu Client."""
        self.hide()
        self.master.show()

    def update_table(self):
        """Update table."""
        vehicles = self.vehicle.get_vehicles_with_clients_details()
        id = [vehicle.get("vehicle_id") for vehicle in vehicles]
        vehicle_identity = [vehicle.get("vehicle_identity") for vehicle in vehicles]
        mileage = [vehicle.get("mileage") for vehicle in vehicles]
        model = [vehicle.get("model") for vehicle in vehicles]
        brand = [vehicle.get("brand") for vehicle in vehicles]
        year = [vehicle.get("year") for vehicle in vehicles]
        client_name = [vehicle.get("client_name") for vehicle in vehicles]
        client_last_name = [vehicle.get("client_last_name") for vehicle in vehicles]
        client_identity = [vehicle.get("client_identity") for vehicle in vehicles]

        for i in self.treeview.get_children():
            self.treeview.delete(i)

        for vehicle in range(0, len(vehicles)):
            self.treeview.insert('', vehicle, values=(
                id[vehicle],
                vehicle_identity[vehicle],
                mileage[vehicle],
                model[vehicle],
                brand[vehicle],
                year[vehicle],
                client_name[vehicle],
                client_last_name[vehicle],
                client_identity[vehicle]
            ))
