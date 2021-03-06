import tkinter as tk
from tkinter import ttk

from backend.exceptions.vehicle_type_exceptions import VehicleTypeDeleteException, VehicleTypeGetCategoryException
from graphic_interface.menus.base_frame import BaseFrame
from graphic_interface.menus.vehicle_type.form_edit_vehicle_type import FormEditVehicleType
from graphic_interface.menus.vehicle_type.form_new_vehicle_type import FormNewVehicleType


class MenuVehicleType(BaseFrame):
    """Class for Table Edit Vehicle Type Window."""

    def __init__(self, root, connection, master):
        """Edit Vehicle Type Window init."""
        super().__init__(root=root, connection=connection)
        self.root.state('zoomed')
        self.root['bg'] = 'black'
        self.master = master
        self.data = {
            "brand": tk.StringVar(),
            "model": tk.StringVar(),
            "year": tk.StringVar()
        }

        frame_1 = tk.LabelFrame(self.root, text="Menu Tipo de Vehiculo", width=100, height=10, bg="black", foreground="white", font='bold')
        frame_1.pack(side='top', padx=5, pady=5, fill='x')

        frame_2 = tk.LabelFrame(self.root, width=100, height=10, bg='black')
        frame_2.pack(side='left', ipadx=100, padx=5, pady=5, fill='y')

        frame_3 = tk.LabelFrame(self.root, bg='black')
        frame_3.pack(side='left', padx=5, pady=5, fill='both', expand=True)

        button_1 = tk.Button(frame_2, text="Nuevo", font='Helvetica 20 bold', width=15, bg="gold2", command=self.create_new_vehicle_type)
        button_1.pack(fill='both', pady=10, padx=10)

        button_2 = tk.Button(frame_2, text="Editar", font='Helvetica 20 bold', width=15, bg="gold2", command=self.form_edit_vehicle_type)
        button_2.pack(fill='both', pady=10, padx=10)

        button_3 = tk.Button(frame_2, text="Borrar", font='Helvetica 20 bold', width=15, bg="gold2", command=self.delete_vehicle_type)
        button_3.pack(fill='both', pady=10, padx=10)

        button_4 = tk.Button(frame_2, text="Refrescar Tabla", font='Helvetica 20 bold', bg="gold2", command=self.refresh_table)
        button_4.pack(fill='both', pady=10, padx=10)

        frame_4 = tk.Frame(frame_2, bg='black')
        frame_4.pack(side='bottom', fill='x')

        button_5 = tk.Button(frame_4, text="Regresar", font='Helvetica 15 bold', bg="gold2", command=self.go_back)
        button_5.pack(side='left', pady=10, padx=10)

        # Define search frame
        self.option_var = tk.StringVar()
        self.option_var.set("--Seleccione una busqueda--")
        contents = {"Marca", "Modelo", "Año"}
        self.options = tk.OptionMenu(frame_1, self.option_var, *contents)
        self.options.config(font=('Helvetica', 15), bg="gold2")
        self.options.pack(side='left', pady=10, padx=10, fill='x')

        self.entry_var = tk.StringVar()
        entry = tk.Entry(frame_1, font="Helvetica 15", textvariable=self.entry_var)
        entry.pack(side='left', pady=10, padx=10, fill='x')

        button_6 = tk.Button(frame_1, text="Buscar", font='Helvetica 15 bold', bg="gold2", command=self.search_vehicle_type_by_category)
        button_6.pack(side='left', pady=10, padx=10, fill='x')

        # Define Heading table
        columns = ("Id", "Marca", "Modelo", "Año")
        self.treeview = ttk.Treeview(frame_3, height=18, show="headings", columns=columns)
        self.treeview.heading("Id", text="Id")
        self.treeview.heading("Marca", text="Marca")
        self.treeview.heading("Modelo", text="Modelo")
        self.treeview.heading("Año", text="Año")

        # Define Columns table
        self.treeview.column("Id", stretch=0, width=20, anchor='center')
        self.treeview.column("Marca",width=150, anchor='center')
        self.treeview.column("Modelo", width=150, anchor='center')
        self.treeview.column("Año", width=150, anchor='center')

        # Insert Data
        vehicle_types = self.vehicle_type.get_all()
        id = [vehicle_type.get("vehicle_type_id") for vehicle_type in vehicle_types]
        brand = [vehicle_type.get("brand") for vehicle_type in vehicle_types]
        model = [vehicle_type.get("model") for vehicle_type in vehicle_types]
        year = [vehicle_type.get("year") for vehicle_type in vehicle_types]

        for vehicle_type in range(0, len(vehicle_types)):
            self.treeview.insert('', vehicle_type, values=(
                id[vehicle_type],
                brand[vehicle_type],
                model[vehicle_type],
                year[vehicle_type]))

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

    def create_new_vehicle_type(self):
        """Create new vehicle type."""
        self.new_window = tk.Toplevel(self.root)
        self.app = FormNewVehicleType(root=self.new_window, connection=self.connection, master=self)

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
            self.show_error(message="Por favor seleccione un tipo de vehiulo.")
        else:
            id = values[0]
            response = self.ask_question(
                message_1="Borrar tipo de vehiculo",
                message_2="Esta seguro de eliminar este tipo de vehiculo?"
            )
            if response:
                try:
                    self.vehicle_type.delete(vehicle_type_id=id)
                    self.refresh_table()
                    self.show_info(message=f"El tipo de vehiculo ha sido borrado exitosamente.")
                except VehicleTypeDeleteException as error:
                    if "vehicle registered" in error.message:
                        self.show_error(message=f"Hay un(unos) vehiculo(s) registrado(s) con este tipo de vehiculo. Por favor, borre el vehiculo y luego el tipo de vehiculo.")
                    self.show_error(message=f"Error al borrar el tipo de vehiculo.")

    def get_vehicle_type_by_category(self):
        """Get vehicle type by category."""
        try:
            item = {
                "Marca": self.vehicle_type.get_by_brand(brand=self.entry_var.get()),
                "Modelo": self.vehicle_type.get_by_model(model=self.entry_var.get()),
                "Año": self.vehicle_type.get_by_year(year=self.entry_var.get())
            }
        except VehicleTypeGetCategoryException:
            self.show_error(message=f"Error al buscar el tipo de vehiculo.")
            raise VehicleTypeGetCategoryException()
        return item[self.option_var.get()]

    def search_vehicle_type_by_category(self):
        """Search vehicle type by category."""
        vehicle_types = self.get_vehicle_type_by_category()
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

    def refresh_table(self):
        """Refresh table."""
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
