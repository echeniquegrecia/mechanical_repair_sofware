import tkinter as tk
from tkinter import ttk
from graphic_interface.menus.base_frame import BaseFrame

class FormNewVehicle(BaseFrame):
    """Class for Form New Vehicle window."""

    def __init__(self, root, connection, master):
        """FornNewVehicle init."""
        super().__init__(root=root, connection=connection)
        self.master = master

        self.name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.identity_card = tk.StringVar()
        self.email = tk.StringVar()
        self.phone_1 = tk.StringVar()
        self.phone_2 = tk.StringVar()
        self.address = tk.StringVar()

        self.data_vehicle = {
            "identity": tk.StringVar(),
            "mileage": tk.StringVar()
        }

        # Frame search clients
        frame = tk.LabelFrame(self.root, text="Buscar cliente", font='Helvetica 12 bold')
        frame.pack(side="top", padx=5, pady=5, fill='x')

        # Frame Clients
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

        # Frame Vehicle
        frame_11 = tk.LabelFrame(self.root, text="Inserte los datos del vehiculo", font='Helvetica 12 bold')
        frame_11.pack(side="top", padx=5, pady=5, fill='x')

        frame_12 = tk.Frame(frame_11)
        frame_12.pack(side="top", padx=5, pady=5, fill='x')

        frame_13 = tk.Frame(frame_12)
        frame_13.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_14 = tk.Frame(frame_12)
        frame_14.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_15 = tk.Frame(frame_12)
        frame_15.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_16 = tk.Frame(frame_12)
        frame_16.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_17 = tk.Frame(frame_11)
        frame_17.pack(side="top", fill='x', padx=5, pady=5, expand=True)

        # Frame Buttons
        frame_10 = tk.Frame(self.root)
        frame_10.pack(side="bottom", padx=5, pady=5, fill='x')

        # Frame tests
        frame_18 = tk.Frame(self.root)
        frame_18.pack(side="top", padx=5, pady=5, fill='x')

        # Testing
        self.test = tk.StringVar()
        self.test.trace_add("write", self.callback_test)

        self.test_chosen = ttk.Combobox(frame, width=20, font='Helvetica 18 bold', state="readonly",
                                        textvariable=self.test)
        self.test_chosen["values"] = self.test_client()
        self.test_chosen.pack(side="top", padx=5, pady=5, fill='x', expand=True)

        # Client Data
        name_label = tk.Label(frame_3, text="Nombre", font='Helvetica 18 bold', anchor='w')
        name_label.pack(padx=5, pady=5, fill='both')
        name_entry = tk.Entry(frame_4, font="Helvetica 17", textvariable=self.name)
        name_entry.config(state='readonly')
        name_entry.pack(padx=5, pady=5, fill='both')

        last_name_label = tk.Label(frame_5, text="Apellido", font='Helvetica 18 bold', anchor='w')
        last_name_label.pack(padx=5, pady=5, fill='both')
        last_name_entry = tk.Entry(frame_6, font="Helvetica 17", textvariable=self.last_name)
        last_name_entry.config(state='readonly')
        last_name_entry.pack(padx=5, pady=5, fill='both')

        identity_card_label = tk.Label(frame_3, text="Cedula", font='Helvetica 18 bold', anchor='w')
        identity_card_label.pack(padx=5, pady=5, fill='both')
        identity_card_entry = tk.Entry(frame_4, font="Helvetica 17", textvariable=self.identity_card)
        identity_card_entry.config(state='readonly')
        identity_card_entry.pack(padx=5, pady=5, fill='both')

        email_label = tk.Label(frame_5, text="Email", font='Helvetica 18 bold', anchor='w')
        email_label.pack(padx=5, pady=5, fill='both')
        email_entry = tk.Entry(frame_6, font="Helvetica 17", textvariable=self.email)
        email_entry.config(state='readonly')
        email_entry.pack(padx=5, pady=5, fill='both')

        phone_1_label = tk.Label(frame_3, text="Telefono fijo", font='Helvetica 18 bold', anchor='w')
        phone_1_label.pack(padx=5, pady=5, fill='both')
        phone_1_entry = tk.Entry(frame_4, font="Helvetica 17", textvariable=self.phone_1)
        phone_1_entry.config(state='readonly')
        phone_1_entry.pack(padx=5, pady=5, fill='both')

        phone_2_label = tk.Label(frame_5, text="Celular", font='Helvetica 18 bold', anchor='w')
        phone_2_label.pack(padx=5, pady=5, fill='both')
        phone_2_entry = tk.Entry(frame_6, font="Helvetica 17", textvariable=self.phone_2)
        phone_2_entry.config(state='readonly')
        phone_2_entry.pack(padx=5, pady=5, fill='both')

        address_label = tk.Label(frame_8, text="Direccion", font='Helvetica 18 bold', anchor='w')
        address_label.pack(padx=5, pady=5, fill='both')
        address_entry = tk.Entry(frame_9, font="Helvetica 17", textvariable=self.address)
        address_entry.config(state='readonly')
        address_entry.pack(padx=5, pady=5, fill='both')

        # Vehicle Data
        identity_label = tk.Label(frame_13, text="Placa", font='Helvetica 18 bold', anchor='w')
        identity_label.pack(padx=5, pady=5, fill='both')
        identity_entry = tk.Entry(frame_14, font="Helvetica 17", textvariable=self.data_vehicle["identity"])
        identity_entry.pack(padx=5, pady=5, fill='both')

        mileage_label = tk.Label(frame_15, text="Kilometraje", font='Helvetica 18 bold', anchor='w')
        mileage_label.pack(padx=5, pady=5, fill='both')
        mileage_entry = tk.Entry(frame_16, font="Helvetica 17", textvariable=self.data_vehicle["mileage"])
        mileage_entry.pack(padx=5, pady=5, fill='both')

        number_label = tk.Label(frame_17, text="Tipo de Vehiculo", font='Helvetica 18 bold', anchor='w')
        number_label.pack(side='left', padx=5, pady=5, fill='both')


        self.brand = tk.StringVar()
        self.brand.trace_add("write", self.callback)
        self.model = tk.StringVar()
        self.model.trace_add("write", self.callback)
        self.year = tk.StringVar()

        self.brand_chosen = ttk.Combobox(frame_17, width=20, font='Helvetica 18 bold', textvariable=self.brand, state="readonly")
        self.brand_chosen["values"] = self.get_vehicle_type_brands()
        self.brand_chosen.pack(side='left', padx=5, pady=5, expand=True)

        self.model_chosen = ttk.Combobox(frame_17, width=20, font='Helvetica 18 bold', textvariable=self.model, state="readonly")
        self.model_chosen.pack(side='left', padx=5, pady=5, expand=True)

        self.year_chosen = ttk.Combobox(frame_17, width=20, font='Helvetica 18 bold', textvariable=self.year, state="readonly")
        self.year_chosen.pack(side='left', padx=5, pady=5, expand=True)

        button_1 = tk.Button(frame_10, text="Crear", font='Helvetica 15 bold', width=15, command=self.get_vehicle_type_brands)
        button_1.pack(side='right', fil='x')

        button_2 = tk.Button(frame_10, text="Regresar", font='Helvetica 15 bold', width=15)
        button_2.pack(side='right', fil='x')

        self.root.mainloop()


    def get_vehicle_type_brands(self):
        """Get the vehicle type brands."""
        all_brands = [vehicle_type.get("brand") for vehicle_type in self.vehicle_type.get_all()]
        filter_brands = set(all_brands)
        brands_list = [*filter_brands]
        return brands_list

    def get_vehicle_type_models(self, brand:str):
        """Get the vehicle type models."""
        models = []
        for vehicle_type in self.vehicle_type.get_all():
            if vehicle_type.get("brand") == brand:
                models.append(vehicle_type.get("model"))
        return models

    def get_vehicle_type_year(self, model:str):
        """Get the vehicle type tear."""
        models = []
        for vehicle_type in self.vehicle_type.get_all():
            if vehicle_type.get("model") == model:
                models.append(vehicle_type.get("year"))
        return models


    def callback(self, *args):
        brand = self.brand.get()
        model = self.model.get()
        self.model_chosen.config(values=self.get_vehicle_type_models(brand=brand))
        self.year_chosen.config(values=self.get_vehicle_type_year(model=model))

    def callback_test(self, *args):
        test = self.test.get()
        print(f"test: {test}")

        list = test.split(' ')
        # print(list)
        client = self.client.get_by_id(client_id=list[0])
        self.name.set(client.get("name"))
        self.last_name.set(client.get("last_name"))
        self.identity_card.set(client.get("identity_card"))
        self.email.set(client.get("email"))
        self.phone_1.set(client.get("phone_1"))
        self.phone_2.set(client.get("phone_2"))
        self.address.set(client.get("address"))


    def test_client(self):
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

