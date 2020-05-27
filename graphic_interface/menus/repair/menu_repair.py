import tkinter as tk
from tkinter import ttk
from graphic_interface.menus.base_frame import BaseFrame
from graphic_interface.menus.repair.form_check_details_repair import FormCheckDetailsRepair
from graphic_interface.menus.repair.form_edit_repair import FormEditRepair
from graphic_interface.menus.repair.form_new_repair import FormNewRepair


class MenuRepair(BaseFrame):
    """Class for Menu Repair Window."""

    def __init__(self, root, connection, master):
        """Menu Repair Window init."""
        super().__init__(root=root, connection=connection)
        self.root.state('zoomed')
        self.master = master
        self.option_var = tk.StringVar()
        self.entry_var = tk.StringVar()

        frame_1 = tk.LabelFrame(self.root, text="Menu Reparacion", width=100, height=10)
        frame_1.pack(side='top', padx=5, pady=5, fill='x')

        frame_2 = tk.LabelFrame(self.root, width=100, height=10)
        frame_2.pack(side='left', ipadx=100, padx=5, pady=5, fill='y')

        frame_3 = tk.LabelFrame(self.root)
        frame_3.pack(side='left', padx=5, pady=5, fill='both', expand=True)

        frame_4 = tk.Frame(frame_2)
        frame_4.pack(side='bottom', fill='x')

        button_1 = tk.Button(frame_2, text="Nuevo", font='Helvetica 20 bold', width=15, command=self.create_new_repair)
        button_1.pack(fill='both', pady=10, padx=10)

        button_2 = tk.Button(frame_2, text="Editar", font='Helvetica 20 bold', width=15, command=self.edit_repair)
        button_2.pack(fill='both', pady=10, padx=10)

        button_3 = tk.Button(frame_2, text="Borrar", font='Helvetica 20 bold', width=15, command=self.delete_repair)
        button_3.pack(fill='both', pady=10, padx=10)

        button_5 = tk.Button(frame_2, text="Ver Detalles", font='Helvetica 20 bold', width=15, command=self.check_details_repair)
        button_5.pack(fill='both', pady=10, padx=10)

        button_4 = tk.Button(frame_2, text="Actualizar", font='Helvetica 20 bold', width=15, command=self.update_table)
        button_4.pack(fill='both', pady=10, padx=10)

        button_6 = tk.Button(frame_4, text="Regresar", font='Helvetica 15 bold', command=self.go_back)
        button_6.pack(side='left', pady=10, padx=10)

        # Define search frame
        self.option_var.set("--Seleccione una busqueda--")
        contents = {"Estado"}
        self.options = tk.OptionMenu(frame_1, self.option_var, *contents)
        self.options.config(font=('Helvetica', 15))
        self.options.pack(side='left', pady=10, padx=10, fill='x')
        entry = tk.Entry(frame_1, font="Helvetica 15", textvariable=self.entry_var)
        entry.pack(side='left', pady=10, padx=10, fill='x')
        button_7 = tk.Button(frame_1, text="Buscar", font='Helvetica 15 bold', command=self.search_vehicle_by_category)
        button_7.pack(side='left', pady=10, padx=10, fill='x')

        # Define Heading table
        columns = (
            "Reparacion Id",
            "Estado",
            "Fecha de entrada",
            "Fecha de salida",
            "Placa",
            "Marca",
            "Modelo",
            "Año",
            "Kilometraje",
            "Nombre",
            "Apellido",
            "Cedula"
        )
        self.treeview = ttk.Treeview(frame_3, height=18, show="headings", columns=columns)
        self.treeview.heading("Reparacion Id", text="Reparacion Id")
        self.treeview.heading("Estado", text="Estado")
        self.treeview.heading("Fecha de entrada", text="Fecha de entrada")
        self.treeview.heading("Fecha de salida", text="Fecha de salida")
        self.treeview.heading("Placa", text="Placa")
        self.treeview.heading("Marca", text="Marca")
        self.treeview.heading("Modelo", text="Modelo")
        self.treeview.heading("Año", text="Año")
        self.treeview.heading("Kilometraje", text="Kilometraje")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Apellido", text="Apellido")
        self.treeview.heading("Cedula", text="Cedula")

        # Define Columns table
        self.treeview.column("Reparacion Id", stretch=0, width=80, anchor='center')
        self.treeview.column("Estado",width=80, anchor='center')
        self.treeview.column("Fecha de entrada", width=100, anchor='center')
        self.treeview.column("Fecha de salida", width=100, anchor='center')
        self.treeview.column("Placa", width=80, anchor='center')
        self.treeview.column("Marca", width=120, anchor='center')
        self.treeview.column("Modelo", width=150, anchor='center')
        self.treeview.column("Año", width=50, anchor='center')
        self.treeview.column("Kilometraje", width=120, anchor='center')
        self.treeview.column("Nombre", width=150, anchor='center')
        self.treeview.column("Apellido", width=150, anchor='center')
        self.treeview.column("Cedula", width=150, anchor='center')

        # Insert Data
        repairs = self.repair.get_all_repairs_with_details()
        repair_id = [repair.get("repair_id") for repair in repairs]
        status = [repair.get("status") for repair in repairs]
        date_entry = [repair.get("date_entry") for repair in repairs]
        date_exit = [repair.get("date_exit") for repair in repairs]
        identity = [repair.get("identity") for repair in repairs]
        brand = [repair.get("brand") for repair in repairs]
        model = [repair.get("model") for repair in repairs]
        year = [repair.get("year") for repair in repairs]
        mileage = [repair.get("mileage") for repair in repairs]
        client_name = [repair.get("client_name") for repair in repairs]
        client_last_name = [repair.get("client_last_name") for repair in repairs]
        client_identity = [repair.get("client_identity") for repair in repairs]

        for repair in range(0, len(repairs)):
            self.treeview.insert('', repair, values=(
                repair_id[repair],
                status[repair],
                date_entry[repair],
                date_exit[repair],
                identity[repair],
                brand[repair],
                model[repair],
                year[repair],
                mileage[repair],
                client_name[repair],
                client_last_name[repair],
                client_identity[repair],

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

    def create_new_repair(self):
        """Create new vehicle."""
        self.new_window = tk.Toplevel(self.root)
        self.app = FormNewRepair(
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
        vehicle_id = [vehicle.get("vehicle_id") for vehicle in vehicles]
        vehicle_identity = [vehicle.get("vehicle_identity") for vehicle in vehicles]
        mileage = [vehicle.get("mileage") for vehicle in vehicles]
        model = [vehicle.get("model") for vehicle in vehicles]
        brand = [vehicle.get("brand") for vehicle in vehicles]
        year = [vehicle.get("year") for vehicle in vehicles]
        client_id = [vehicle.get("client_id") for vehicle in vehicles]
        client_name = [vehicle.get("client_name") for vehicle in vehicles]
        client_last_name = [vehicle.get("client_last_name") for vehicle in vehicles]
        client_identity = [vehicle.get("client_identity") for vehicle in vehicles]

        for i in self.treeview.get_children():
            self.treeview.delete(i)

        for vehicle in range(0, len(vehicles)):
            self.treeview.insert('', vehicle, values=(
                vehicle_id[vehicle],
                vehicle_identity[vehicle],
                mileage[vehicle],
                model[vehicle],
                brand[vehicle],
                year[vehicle],
                client_id[vehicle],
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
        repairs = self.repair.get_all_repairs_with_details()
        repair_id = [repair.get("repair_id") for repair in repairs]
        status = [repair.get("status") for repair in repairs]
        date_entry = [repair.get("date_entry") for repair in repairs]
        date_exit = [repair.get("date_exit") for repair in repairs]
        identity = [repair.get("identity") for repair in repairs]
        brand = [repair.get("brand") for repair in repairs]
        model = [repair.get("model") for repair in repairs]
        year = [repair.get("year") for repair in repairs]
        mileage = [repair.get("mileage") for repair in repairs]
        client_name = [repair.get("client_name") for repair in repairs]
        client_last_name = [repair.get("client_last_name") for repair in repairs]
        client_identity = [repair.get("client_identity") for repair in repairs]

        for i in self.treeview.get_children():
            self.treeview.delete(i)

        for repair in range(0, len(repairs)):
            self.treeview.insert('', repair, values=(
                repair_id[repair],
                status[repair],
                date_entry[repair],
                date_exit[repair],
                identity[repair],
                brand[repair],
                model[repair],
                year[repair],
                mileage[repair],
                client_name[repair],
                client_last_name[repair],
                client_identity[repair],

            ))

    def edit_repair(self):
        """Open Form Edit Repair."""
        values = self.get_values()
        if not values:
            self.show_error(message="Por favor seleccione un vehiculo.")
        else:
            self.new_window = tk.Toplevel(self.root)
            self.app = FormEditRepair(root=self.new_window, connection=self.connection, master=self, values=values)

    def check_details_repair(self):
        """Open Form Edit Repair."""
        values = self.get_values()
        if not values:
            self.show_error(message="Por favor seleccione un vehiculo.")
        else:
            self.new_window = tk.Toplevel(self.root)
            self.app = FormCheckDetailsRepair(root=self.new_window, connection=self.connection, master=self, values=values)

    def delete_repair(self):
        """Delete repair."""
        values = self.get_values()
        if not values:
            self.show_error(message="Por favor seleccione una reparacion.")
        else:
            repair_id = values[0]
            self.repair.delete(repair_id=repair_id)
            self.update_table()
            self.show_info(message=f"La reparacion ha sido borrada exitosamente.")