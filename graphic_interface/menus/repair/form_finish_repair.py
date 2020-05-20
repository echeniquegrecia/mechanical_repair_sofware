import tkinter as tk
from tkcalendar import DateEntry
from graphic_interface.menus.base_frame import BaseFrame

class FormFinishRepair(BaseFrame):
    """Class for Form Edit Repair window."""

    def __init__(self, root, connection, master, values):
        """FormFinishRepair init."""
        super().__init__(root=root, connection=connection)
        self.root.state('zoomed')
        self.repair_id = values[0]
        self.data = self.repair.get_by_id(repair_id=self.repair_id)[0]
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
        self.vehicle_id = tk.StringVar()
        self.vehicle_identity = tk.StringVar()
        self.color = tk.StringVar()
        self.brand = tk.StringVar()
        self.model = tk.StringVar()
        self.year = tk.StringVar()
        self.status = tk.StringVar()
        self.mileage = tk.StringVar()
        self.client_obs = tk.StringVar()
        self.mechanical_obs = tk.StringVar()
        self.price = tk.StringVar()
        self.date_entry = tk.StringVar()

        frame_1 = tk.LabelFrame(self.root, text="Datos del cliente", font='Helvetica 11 bold')
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

        name_label = tk.Label(frame_3, text="Nombre", font='Helvetica 11 bold', anchor='w')
        name_label.pack(padx=5, pady=5, fill='both')
        name_entry = tk.Entry(frame_4, font="Helvetica 12", textvariable=self.name)
        self.name.set(self.data.get("client_name"))
        name_entry.config(state='readonly')
        name_entry.pack(padx=5, pady=5, fill='both')

        last_name_label = tk.Label(frame_5, text="Apellido", font='Helvetica 11 bold', anchor='w')
        last_name_label.pack(padx=5, pady=5, fill='both')
        last_name_entry = tk.Entry(frame_6, font="Helvetica 12", textvariable=self.last_name)
        self.last_name.set(self.data.get("client_last_name"))
        last_name_entry.config(state='readonly')
        last_name_entry.pack(padx=5, pady=5, fill='both')

        identity_card_label = tk.Label(frame_3, text="Cedula", font='Helvetica 11 bold', anchor='w')
        identity_card_label.pack(padx=5, pady=5, fill='both')
        identity_card_entry = tk.Entry(frame_4, font="Helvetica 12", textvariable=self.identity_card)
        self.identity_card.set(self.data.get("client_identity_card"))
        identity_card_entry.config(state='readonly')
        identity_card_entry.pack(padx=5, pady=5, fill='both')

        email_label = tk.Label(frame_5, text="Email", font='Helvetica 11 bold', anchor='w')
        email_label.pack(padx=5, pady=5, fill='both')
        email_entry = tk.Entry(frame_6, font="Helvetica 12", textvariable=self.email)
        self.email.set(self.data.get("client_email"))
        email_entry.config(state='readonly')
        email_entry.pack(padx=5, pady=5, fill='both')

        phone_1_label = tk.Label(frame_3, text="Telefono fijo", font='Helvetica 11 bold', anchor='w')
        phone_1_label.pack(padx=5, pady=5, fill='both')
        phone_1_entry = tk.Entry(frame_4, font="Helvetica 12", textvariable=self.phone_1)
        self.phone_1.set(self.data.get("client_phone_1"))
        phone_1_entry.config(state='readonly')
        phone_1_entry.pack(padx=5, pady=5, fill='both')

        phone_2_label = tk.Label(frame_5, text="Celular", font='Helvetica 11 bold', anchor='w')
        phone_2_label.pack(padx=5, pady=5, fill='both')
        phone_2_entry = tk.Entry(frame_6, font="Helvetica 12", textvariable=self.phone_2)
        self.phone_2.set(self.data.get("client_phone_2"))
        phone_2_entry.config(state='readonly')
        phone_2_entry.pack(padx=5, pady=5, fill='both')

        address_label = tk.Label(frame_8, text="Direccion", font='Helvetica 11 bold', anchor='w')
        address_label.pack(padx=5, pady=5, fill='both')
        address_entry = tk.Entry(frame_9, font="Helvetica 12", textvariable=self.address)
        self.address.set(self.data.get("client_address"))
        address_entry.config(state='readonly')
        address_entry.pack(padx=5, pady=5, fill='both')

        # Frame Vehicle details
        frame_11 = tk.LabelFrame(self.root, text="Datos del vehiculo", font='Helvetica 11 bold')
        frame_11.pack(side="top", padx=5, pady=5, fill='x')

        frame_13 = tk.Frame(frame_11)
        frame_13.pack(side="left", fill='both', padx=5, pady=5, expand=True)

        frame_14 = tk.Frame(frame_11)
        frame_14.pack(side="left", fill='both', padx=5, pady=5, expand=True)

        frame_15 = tk.Frame(frame_11)
        frame_15.pack(side="left", fill='both', padx=5, pady=5, expand=True)

        frame_16 = tk.Frame(frame_11)
        frame_16.pack(side="left", fill='both', padx=5, pady=5, expand=True)

        vehicle_identity_label = tk.Label(frame_13, text="Placa", font='Helvetica 11 bold', anchor='w')
        vehicle_identity_label.pack(padx=5, pady=5, fill='both')
        vehicle_identity_entry = tk.Entry(frame_14, font="Helvetica 12", textvariable=self.vehicle_identity)
        self.vehicle_identity.set(self.data.get("vehicle_identity"))
        vehicle_identity_entry.config(state='readonly')
        vehicle_identity_entry.pack(padx=5, pady=5, fill='both')

        color_label = tk.Label(frame_15, text="Color", font='Helvetica 11 bold', anchor='w')
        color_label.pack(padx=5, pady=5, fill='both')
        color_entry = tk.Entry(frame_16, font="Helvetica 12", textvariable=self.color)
        self.color.set(self.data.get("vehicle_color"))
        color_entry.config(state='readonly')
        color_entry.pack(padx=5, pady=5, fill='both')

        vehicle_type_label = tk.Label(frame_13, text="Tipo de Vehiculo", font='Helvetica 11 bold', anchor='w')
        vehicle_type_label.pack(padx=5, pady=5, fill='both')

        brand_entry = tk.Entry(frame_14, font="Helvetica 12", textvariable=self.brand)
        self.brand.set(self.data.get("vehicle_type_brand"))
        brand_entry.config(state='readonly')
        brand_entry.pack(padx=5, pady=5, fill='both')

        model_entry = tk.Entry(frame_15, font="Helvetica 12", textvariable=self.model)
        self.model.set(self.data.get("vehicle_type_model"))
        model_entry.config(state='readonly')
        model_entry.pack(padx=5, pady=5, fill='both')

        year_entry = tk.Entry(frame_16, font="Helvetica 12", textvariable=self.year)
        self.year.set(self.data.get("vehicle_type_year"))
        year_entry.config(state='readonly')
        year_entry.pack(padx=5, pady=5, fill='both')

        mileage_label = tk.Label(frame_13, text="Kilometraje", font='Helvetica 11 bold', anchor='w')
        mileage_label.pack(padx=5, pady=5, fill='both')
        mileage_entry = tk.Entry(frame_14, font="Helvetica 12", textvariable=self.mileage)
        self.mileage.set(self.data.get("mileage"))
        mileage_entry.pack(padx=5, pady=5, fill='both')

        # Repair details
        frame_17 = tk.LabelFrame(self.root, text="Detalles de la Reparacion", font='Helvetica 11 bold')
        frame_17.pack(side="top", padx=5, pady=5, fill='both')

        frame_test = tk.Frame(frame_17)
        frame_test.pack(side="top", fill='x', padx=5, pady=5, expand=True)

        frame_18 = tk.Frame(frame_test)
        frame_18.pack(side="left", fill='x', padx=5, pady=5, expand=True)
        frame_19 = tk.Frame(frame_test)
        frame_19.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_test_1 = tk.Frame(frame_17)
        frame_test_1.pack(side="top", fill='x', padx=5, pady=5, expand=True)

        # Date Entry
        frame_20 = tk.Frame(frame_18)
        frame_20.pack(side="top", fill='x', padx=5, pady=5, expand=True)
        date_entry_label = tk.Label(frame_20, text="Fecha de entrada:", font='Helvetica 11 bold', anchor='w')
        date_entry_label.pack(side="left", padx=5, pady=5, fill='x', expand=True)
        date_entry = DateEntry(frame_20, width=4, font="Helvetica 12", background='darkblue', foreground='white', borderwidth=1, textvariable=self.date_entry)
        self.date_entry.set(self.data.get("date_entry"))
        date_entry.pack(side="left", padx=5, pady=5, fill='x', expand=True)

        # Client observations
        client_obs_label = tk.Label(frame_18, text="Observaciones del Cliente:", font='Helvetica 11 bold', anchor='w')
        client_obs_label.pack(side="top", padx=5, pady=5, fill='x', expand=True)
        self.client_obs = tk.Text(frame_18, height=4)
        self.client_obs.pack(side="left", fill="x", expand=True)
        self.client_obs.insert(tk.END, self.data.get("client_observations"))
        scrollbar_client = tk.Scrollbar(frame_18)
        scrollbar_client.pack(side="left", fill="y")
        scrollbar_client.config(command=self.client_obs.yview)
        self.client_obs.config(yscrollcommand=scrollbar_client.set)

        # Price
        frame_21 = tk.Frame(frame_19)
        frame_21.pack(side="top", fill='x', padx=5, pady=5, expand=True)
        price_label = tk.Label(frame_21, text="Precio:", font='Helvetica 11 bold', anchor='w')
        price_label.pack(side="left", padx=5, pady=5, fill='x', expand=True)
        price_entry = tk.Entry(frame_21, font="Helvetica 12", textvariable=self.price)
        self.price.set(self.data.get("price"))
        price_entry.pack(side="left", padx=5, pady=5, fill='x', expand=True)

        # Mechanical observations
        mechanical_obs_label = tk.Label(frame_19, text="Observaciones del Mecanico:", font='Helvetica 11 bold', anchor='w')
        mechanical_obs_label.pack(side="top", padx=5, pady=5, fill='x', expand=True)
        scrollbar_mechanical = tk.Scrollbar(frame_19)
        self.mechanical_obs = tk.Text(frame_19, height=4)
        self.mechanical_obs.insert(tk.END, self.data.get("mechanical_observations"))
        self.mechanical_obs.pack(side="left", fill="x", expand=True)
        scrollbar_mechanical.pack(side="left", fill="y")
        scrollbar_mechanical.config(command=self.mechanical_obs.yview)
        self.mechanical_obs.config(yscrollcommand=scrollbar_mechanical.set)

        # Final details
        frame_22 = tk.LabelFrame(self.root, text="Detalles Finales", font='Helvetica 11 bold')
        frame_22.pack(side="top", padx=5, pady=5, fill='both')

        # Date exit
        frame_23 = tk.Frame(frame_22)
        frame_23.pack(side="top", fill='x', padx=5, pady=5, expand=True)
        date_exit_label = tk.Label(frame_23, text="Fecha de salida:", font='Helvetica 11 bold', anchor='w')
        date_exit_label.pack(side="left", padx=5, pady=5, fill='x', expand=True)
        date_exit = DateEntry(frame_23, width=4, font="Helvetica 7", background='darkblue', foreground='white',
                               borderwidth=1)
        #self.date_entry.set(self.data.get("date_exit"))
        date_exit.pack(side="left", padx=5, pady=5, fill='x', expand=True)



        # Buttons
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(side="bottom", padx=5, pady=5, fill='x')

        button_1 = tk.Button(frame_buttons, text="Guardar", font='Helvetica 15 bold', width=15, command=self.edit_repair)
        button_1.pack(side='right', fil='x', padx=5, pady=5)

        button_2 = tk.Button(frame_buttons, text="Regresar", font='Helvetica 15 bold', width=15, command=self.go_back)
        button_2.pack(side='right', fil='x', padx=5, pady=5)

        self.root.mainloop()

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

    def edit_repair(self):
        """Edir repair."""
        repair_data = {
            "vehicle_id": self.data.get("vehicle_id"),
            "mileage": self.mileage.get(),
            "client_observations": self.client_obs.get("1.0", "end"),
            "mechanical_observations": self.mechanical_obs.get("1.0", "end"),
            "final_observations": "",
            "date_entry": self.date_entry.get(),
            "date_exit": "",
            "price": self.price.get(),
            "status": "EN TALLER"
        }
        repair = self.repair.update(repair_id=self.repair_id, data=repair_data)
        if repair:
            self.show_info(message="La reparacion ha sido registrada exitosamente.")
        else:
            self.show_error(message="ERROR: La reparacion no ha sido creada.")
