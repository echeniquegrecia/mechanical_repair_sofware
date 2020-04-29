import tkinter as tk
from tkinter import ttk
from graphic_interface.menus.base_frame import BaseFrame
from graphic_interface.menus.vehicle.form_new_vehicle import FormNewVehicle


class TableNewVehicle(BaseFrame):
    """Class for Table new vehicle."""

    def __init__(self, root, connection, master):
        """Menu Vehicle Window init."""
        super().__init__(root=root, connection=connection)
        self.master = master
        self.data = {
            "brand": tk.StringVar(),
            "model": tk.StringVar(),
            "year": tk.StringVar()
        }

        frame_1 = tk.LabelFrame(self.root, text="Menu Vehiculo", width=100, height=10)
        frame_1.pack(side='top', padx=5, pady=5, fill='x')

        frame_2 = tk.LabelFrame(self.root, width=100, height=10)
        frame_2.pack(side='left', padx=5, pady=5, fill='both', expand=True)

        frame_3 = tk.LabelFrame(self.root)
        frame_3.pack(side='left', padx=5, pady=5, fill='both', expand=True)

        button_1 = tk.Button(frame_2, text="Nuevo", font='Helvetica 20 bold', width=15, command=self.create_new_vehicle)
        button_1.pack(fill='both', pady=10, padx=10)

        button_2 = tk.Button(frame_2, text="Actualizar", font='Helvetica 20 bold', command=self.update_table)
        button_2.pack(fill='both', pady=10, padx=10)

        frame_4 = tk.Frame(frame_2)
        frame_4.pack(side='bottom', fill='x')

        button_5 = tk.Button(frame_4, text="Regresar", font='Helvetica 15 bold', command=self.go_back)
        button_5.pack(side='left', pady=10, padx=10)


        # Define search frame
        self.option_var = tk.StringVar()
        self.option_var.set("--Seleccione una busqueda--")
        contents = {"Marca", "Modelo", "Año"}
        self.options = tk.OptionMenu(frame_1, self.option_var, *contents)
        self.options.config(font=('Helvetica', 15))
        self.options.pack(side='left', pady=10, padx=10, fill='x')

        self.entry_var = tk.StringVar()
        entry = tk.Entry(frame_1, font="Helvetica 15", textvariable=self.entry_var)
        entry.pack(side='left', pady=10, padx=10, fill='x')

        button_6 = tk.Button(frame_1, text="Buscar", font='Helvetica 15 bold', command=self.search_vehicle_type_by_category)
        button_6.pack(side='left', pady=10, padx=10, fill='x')

        # Define Heading table
        columns = ("Id", "Nombre", "Apellido", "Cédula", "Email", "Teléfono fijo", "Celular", "Direccion")
        self.treeview = ttk.Treeview(frame_3, height=18, show="headings", columns=columns)
        self.treeview.heading("Id", text="Id")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Apellido", text="Apellido")
        self.treeview.heading("Cédula", text="Cédula")
        self.treeview.heading("Email", text="Email")
        self.treeview.heading("Teléfono fijo", text="Teléfono fijo")
        self.treeview.heading("Celular", text="Celular")
        self.treeview.heading("Direccion", text="Direccion")

        # Define Columns table
        self.treeview.column("Id", stretch=0, width=20, anchor='center')
        self.treeview.column("Nombre", width=150, anchor='center')
        self.treeview.column("Apellido", width=150, anchor='center')
        self.treeview.column("Cédula", width=150, anchor='center')
        self.treeview.column("Email", width=150, anchor='center')
        self.treeview.column("Teléfono fijo", width=150, anchor='center')
        self.treeview.column("Celular", width=150, anchor='center')
        self.treeview.column("Direccion", width=150, anchor='center')

        # Insert Data
        clients = self.client.get_all()
        id = [client.get("client_id") for client in clients]
        name = [client.get("name") for client in clients]
        last_name = [client.get("last_name") for client in clients]
        identity_card = [client.get("identity_card") for client in clients]
        email = [client.get("email") for client in clients]
        phone_1 = [client.get("phone_1") for client in clients]
        phone_2 = [client.get("phone_2") for client in clients]
        address = [client.get("address") for client in clients]

        for client in range(0, len(clients)):
            self.treeview.insert('', client, values=(
                id[client],
                name[client],
                last_name[client],
                identity_card[client],
                email[client],
                phone_1[client],
                phone_2[client],
                address[client]))

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
        values = self.get_values()
        if not values:
            self.show_error(message="Por favor seleccione un cliente.")
        self.new_window = tk.Toplevel(self.root)
        self.app = FormNewVehicle(root=self.new_window, connection=self.connection, master=self, values=values)


    def form_edit_vehicle_type(self):
        """Open Form Edit Vehicle Edit."""
        values = self.get_values()
        if not values:
            self.show_error(message="Por favor seleccione un cliente.")
        self.new_window = tk.Toplevel(self.root)
        self.app = FormEditVehicleType(root=self.new_window, connection=self.connection, master=self, values=values)

    def delete_vehicle_type(self):
        """Delete Vehicle Edit."""
        values = self.get_values()
        if not values:
            self.show_error(message="Por favor seleccione un cliente.")
        id = values[0]
        brand = values[1]
        model = values[2]
        year = values[3]
        self.vehicle_type.delete(vehicle_type_id=id)
        self.show_error(message=f"El tipo de vehiculo: {brand} {model} {year} ha sido borrado exitosamente.")

    def get_vehicle_type_by_item(self):
        """Get client."""
        item = {
            "Marca": self.vehicle_type.get_by_brand(brand=self.entry_var.get()),
            "Modelo": self.vehicle_type.get_by_model(model=self.entry_var.get()),
            "Año": self.vehicle_type.get_by_year(year=self.entry_var.get())
        }
        return item[self.option_var.get()]


    def search_vehicle_type_by_category(self):
        """Search vehicle type by category."""
        vehicle_types = self.get_vehicle_type_by_item()
        id = [vehicle_type.get("vehicle_type_id") for vehicle_type in vehicle_types]
        brand = [vehicle_type.get("brand") for vehicle_type in vehicle_types]
        model = [vehicle_type.get("model") for vehicle_type in vehicle_types]
        year = [vehicle_type.get("year") for vehicle_type in vehicle_types]

        for i in self.treeview.get_children():
            self.treeview.delete(i)

        for vehicle_type in range(0, len(vehicle_types)):
            self.treeview.insert('', vehicle_type, values=(
                id[vehicle_type],
                brand[vehicle_type],
                model[vehicle_type],
                year[vehicle_type]))

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
        vehicle_types = self.vehicle_type.get_all()
        id = [vehicle_type.get("vehicle_type_id") for vehicle_type in vehicle_types]
        brand = [vehicle_type.get("brand") for vehicle_type in vehicle_types]
        model = [vehicle_type.get("model") for vehicle_type in vehicle_types]
        year = [vehicle_type.get("year") for vehicle_type in vehicle_types]

        for i in self.treeview.get_children():
            self.treeview.delete(i)

        for vehicle_type in range(0, len(vehicle_types)):
            self.treeview.insert('', vehicle_type, values=(
                id[vehicle_type],
                brand[vehicle_type],
                model[vehicle_type],
                year[vehicle_type]))