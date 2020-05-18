import tkinter as tk
from tkinter import ttk
from graphic_interface.menus.base_frame import BaseFrame

class FormNewRepair(BaseFrame):
    """Class for Form New Repair window."""

    def __init__(self, root, connection, master):
        """FormNewRepair init."""
        super().__init__(root=root, connection=connection)
        self.master = master
        self._client = tk.StringVar()
        self._vehicle = tk.StringVar()
        self.client_id = tk.StringVar()
        self.name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.identity_card = tk.StringVar()
        self.email = tk.StringVar()
        self.phone_1 = tk.StringVar()
        self.phone_2 = tk.StringVar()
        self.address = tk.StringVar()
        self.vehicle_identity = tk.StringVar()
        self.color = tk.StringVar()
        self.brand = tk.StringVar()
        self.model = tk.StringVar()
        self.year = tk.StringVar()

        # Frame Search clients
        frame = tk.LabelFrame(self.root, text="Buscar cliente", font='Helvetica 12 bold')
        frame.pack(side="top", padx=5, pady=5, fill='x')

        self._client.trace_add("write", self.callback)
        self.client_chosen = ttk.Combobox(frame, width=20, font='Helvetica 12 bold', state="readonly",
                                          textvariable=self._client)
        self.client_chosen["values"] = self.get_clients()
        self.client_chosen.pack(side="top", padx=5, pady=5, fill='x', expand=True)

        # Frame Details Clients
        frame_1 = tk.LabelFrame(self.root, text="Datos del cliente", font='Helvetica 12 bold')
        frame_1.pack(side="top", padx=5, pady=5, fill='x')

        frame_2 = tk.Frame(frame_1)
        frame_2.pack(side="top", padx=5, pady=5, fill='x')

        frame_3 = tk.Frame(frame_2)
        frame_3.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_4 = tk.Frame(frame_2)
        frame_4.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_5 = tk.Frame(frame_2)
        frame_5.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_6 = tk.Frame(frame_2)
        frame_6.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_7 = tk.Frame(frame_1)
        frame_7.pack(side="top", padx=5, pady=5, fill='x')

        frame_8 = tk.Frame(frame_7)
        frame_8.pack(side="left", fill='x')

        frame_9 = tk.Frame(frame_7)
        frame_9.pack(side="left", fill='x', expand=True)

        name_label = tk.Label(frame_3, text="Nombre", font='Helvetica 12 bold', anchor='w')
        name_label.pack(padx=5, pady=5, fill='both')
        name_entry = tk.Entry(frame_4, font="Helvetica 12", textvariable=self.name)
        name_entry.config(state='readonly')
        name_entry.pack(padx=5, pady=5, fill='both')

        last_name_label = tk.Label(frame_5, text="Apellido", font='Helvetica 12 bold', anchor='w')
        last_name_label.pack(padx=5, pady=5, fill='both')
        last_name_entry = tk.Entry(frame_6, font="Helvetica 12", textvariable=self.last_name)
        last_name_entry.config(state='readonly')
        last_name_entry.pack(padx=5, pady=5, fill='both')

        identity_card_label = tk.Label(frame_3, text="Cedula", font='Helvetica 12 bold', anchor='w')
        identity_card_label.pack(padx=5, pady=5, fill='both')
        identity_card_entry = tk.Entry(frame_4, font="Helvetica 12", textvariable=self.identity_card)
        identity_card_entry.config(state='readonly')
        identity_card_entry.pack(padx=5, pady=5, fill='both')

        email_label = tk.Label(frame_5, text="Email", font='Helvetica 12 bold', anchor='w')
        email_label.pack(padx=5, pady=5, fill='both')
        email_entry = tk.Entry(frame_6, font="Helvetica 12", textvariable=self.email)
        email_entry.config(state='readonly')
        email_entry.pack(padx=5, pady=5, fill='both')

        phone_1_label = tk.Label(frame_3, text="Telefono fijo", font='Helvetica 12 bold', anchor='w')
        phone_1_label.pack(padx=5, pady=5, fill='both')
        phone_1_entry = tk.Entry(frame_4, font="Helvetica 12", textvariable=self.phone_1)
        phone_1_entry.config(state='readonly')
        phone_1_entry.pack(padx=5, pady=5, fill='both')

        phone_2_label = tk.Label(frame_5, text="Celular", font='Helvetica 12 bold', anchor='w')
        phone_2_label.pack(padx=5, pady=5, fill='both')
        phone_2_entry = tk.Entry(frame_6, font="Helvetica 12", textvariable=self.phone_2)
        phone_2_entry.config(state='readonly')
        phone_2_entry.pack(padx=5, pady=5, fill='both')

        address_label = tk.Label(frame_8, text="Direccion", font='Helvetica 12 bold', anchor='w')
        address_label.pack(padx=5, pady=5, fill='both')
        address_entry = tk.Entry(frame_9, font="Helvetica 12", textvariable=self.address)
        address_entry.config(state='readonly')
        address_entry.pack(padx=5, pady=5, fill='both')

        # Frame Search vehicle
        frame_10 = tk.LabelFrame(self.root, text="Buscar vehiculo", font='Helvetica 12 bold')
        frame_10.pack(side="top", padx=5, pady=5, fill='x')

        self._vehicle.trace_add("write", self.callback_test)
        self.vehicle_chosen = ttk.Combobox(frame_10, width=20, font='Helvetica 12 bold', state="readonly",textvariable=self._vehicle)
        self.vehicle_chosen.pack(side="top", padx=5, pady=5, fill='x', expand=True)

        # Frame Vehicle details
        frame_11 = tk.LabelFrame(self.root, text="Datos del vehiculo", font='Helvetica 12 bold')
        frame_11.pack(side="top", padx=5, pady=5, fill='x')

        frame_13 = tk.Frame(frame_11)
        frame_13.pack(side="left", fill='both', padx=5, pady=5, expand=True)

        frame_14 = tk.Frame(frame_11)
        frame_14.pack(side="left", fill='both', padx=5, pady=5, expand=True)

        frame_15 = tk.Frame(frame_11)
        frame_15.pack(side="left", fill='both', padx=5, pady=5, expand=True)

        frame_16 = tk.Frame(frame_11)
        frame_16.pack(side="left", fill='both', padx=5, pady=5, expand=True)

        self.vehicle_identity.trace_add("write", self.callback_test)
        self.color.trace_add("write", self.callback_test)
        self.brand.trace_add("write", self.callback_test)
        self.model.trace_add("write", self.callback_test)
        self.year.trace_add("write", self.callback_test)

        vehicle_identity_label = tk.Label(frame_13, text="Placa", font='Helvetica 12 bold', anchor='w')
        vehicle_identity_label.pack(padx=5, pady=5, fill='both')
        vehicle_identity_entry = tk.Entry(frame_14, font="Helvetica 12", textvariable=self.vehicle_identity)
        vehicle_identity_entry.config(state='readonly')
        vehicle_identity_entry.pack(padx=5, pady=5, fill='both')

        color_label = tk.Label(frame_15, text="Color", font='Helvetica 12 bold', anchor='w')
        color_label.pack(padx=5, pady=5, fill='both')
        color_entry = tk.Entry(frame_16, font="Helvetica 12", textvariable=self.color)
        color_entry.config(state='readonly')
        color_entry.pack(padx=5, pady=5, fill='both')

        vehicle_type_label = tk.Label(frame_13, text="Tipo de Vehiculo", font='Helvetica 12 bold', anchor='w')
        vehicle_type_label.pack(padx=5, pady=5, fill='both')

        brand_entry = tk.Entry(frame_14, font="Helvetica 12", textvariable=self.brand)
        brand_entry.config(state='readonly')
        brand_entry.pack(padx=5, pady=5, fill='both')

        model_entry = tk.Entry(frame_15, font="Helvetica 12", textvariable=self.model)
        model_entry.config(state='readonly')
        model_entry.pack(padx=5, pady=5, fill='both')

        year_entry = tk.Entry(frame_16, font="Helvetica 12", textvariable=self.year)
        year_entry.config(state='readonly')
        year_entry.pack(padx=5, pady=5, fill='both')

        mileage_label = tk.Label(frame_13, text="Kilometraje", font='Helvetica 12 bold', anchor='w')
        mileage_label.pack(padx=5, pady=5, fill='both')
        mileage_entry = tk.Entry(frame_14, font="Helvetica 12")
        mileage_entry.pack(padx=5, pady=5, fill='both')




        self.root.mainloop()

    def callback(self, *args):
        client = self._client.get()
        list = client.split(' ')
        client = self.client.get_by_id(client_id=list[0])[0]
        self.client_id.set(client.get("client_id"))
        self.name.set(client.get("name"))
        self.last_name.set(client.get("last_name"))
        self.identity_card.set(client.get("identity_card"))
        self.email.set(client.get("email"))
        self.phone_1.set(client.get("phone_1"))
        self.phone_2.set(client.get("phone_2"))
        self.address.set(client.get("address"))
        vehicles = self.get_vehicles(client_id=list[0])
        self.vehicle_chosen.config(values=vehicles)

    def callback_test(self, *args):
        vehicle = self._vehicle.get()
        vehicle_id = vehicle.split(' ')[0]
        vehicle = self.vehicle.get_by_vehicle_type_id_with_details(vehicle_id=vehicle_id)[0]
        self.vehicle_identity.set(vehicle.get("identity"))
        self.color.set(vehicle.get("color"))
        self.model.set(vehicle.get("model"))
        self.brand.set(vehicle.get("brand"))
        self.year.set(vehicle.get("year"))

    def go_back(self):
        """Go back to Menu Client."""
        self.hide()
        self.master.show()

    def get_clients(self):
        list = []
        clients = self.client.get_all()
        for client in clients:
            list.append([
                client.get("client_id"),
                client.get("name"),
                client.get("last_name"),
                client.get("identity_card"),
                client.get("email"),
                client.get("address")
            ])
        return list

    def get_vehicles(self, client_id):
        vehicles = self.vehicle.get_vehicles_with_clients_details()
        list = []
        for vehicle in vehicles:
            if vehicle.get("client_id") == int(client_id):
                list.append([
                    vehicle.get("vehicle_id"),
                    vehicle.get("brand"),
                    vehicle.get("model"),
                    vehicle.get("year"),
                    vehicle.get("color"),
                    vehicle.get("vehicle_identity"),
                ])
        return list