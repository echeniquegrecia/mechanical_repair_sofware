import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from graphic_interface.menus.base_frame import BaseFrame


class FormEditRepair(BaseFrame):
    """Class for Form Edit Repair window."""

    def __init__(self, root, connection, master, values):
        """FormEditRepair init."""
        super().__init__(root=root, connection=connection)
        self.root.state('zoomed')
        self.master = master
        self.repair_id = values[0]
        self.data = self.repair.get_by_id(repair_id=self.repair_id)[0]
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
        self.status_selected = tk.StringVar()
        self.mileage = tk.StringVar()
        self.client_obs = tk.StringVar()
        self.mechanical_obs = tk.StringVar()
        self.final_obs = tk.StringVar()
        self.price = tk.StringVar()
        self.date_entry = tk.StringVar()
        self.date_exit = tk.StringVar()

        # Frame Details Clients
        frame_details_client = tk.LabelFrame(self.root, text="Datos del cliente", font='Helvetica 12 bold')
        frame_details_client.pack(side="top", padx=5, pady=5, fill='x')

        frame_details_client_1 = tk.Frame(frame_details_client)
        frame_details_client_1.pack(side="top", fill='x')

        frame_details_client_2 = tk.Frame(frame_details_client_1)
        frame_details_client_2.pack(side="left", fill='x', expand=True)

        frame_details_client_3 = tk.Frame(frame_details_client_1)
        frame_details_client_3.pack(side="left", fill='x', expand=True)

        frame_details_client_4 = tk.Frame(frame_details_client_1)
        frame_details_client_4.pack(side="left", fill='x', expand=True)

        frame_details_client_5 = tk.Frame(frame_details_client_1)
        frame_details_client_5.pack(side="left", fill='x', expand=True)

        frame_details_client_6 = tk.Frame(frame_details_client)
        frame_details_client_6.pack(side="top", fill='x')

        frame_details_client_7 = tk.Frame(frame_details_client_6)
        frame_details_client_7.pack(side="left", fill='x')

        frame_details_client_8 = tk.Frame(frame_details_client_6)
        frame_details_client_8.pack(side="left", fill='x', expand=True)

        name_label = tk.Label(frame_details_client_2, text="Nombre", font='Helvetica 12 bold', anchor='w')
        name_label.pack(padx=5, pady=5, fill='both')
        name_entry = tk.Entry(frame_details_client_3, font="Helvetica 12", textvariable=self.name)
        self.name.set(self.data.get("client_name"))
        name_entry.config(state='readonly')
        name_entry.pack(padx=5, pady=5, fill='both')

        last_name_label = tk.Label(frame_details_client_4, text="Apellido", font='Helvetica 12 bold', anchor='w')
        last_name_label.pack(padx=5, pady=5, fill='both')
        last_name_entry = tk.Entry(frame_details_client_5, font="Helvetica 12", textvariable=self.last_name)
        self.last_name.set(self.data.get("client_last_name"))
        last_name_entry.config(state='readonly')
        last_name_entry.pack(padx=5, pady=5, fill='both')

        identity_card_label = tk.Label(frame_details_client_2, text="Cedula", font='Helvetica 12 bold', anchor='w')
        identity_card_label.pack(padx=5, pady=5, fill='both')
        identity_card_entry = tk.Entry(frame_details_client_3, font="Helvetica 12", textvariable=self.identity_card)
        self.identity_card.set(self.data.get("client_identity_card"))
        identity_card_entry.config(state='readonly')
        identity_card_entry.pack(padx=5, pady=5, fill='both')

        email_label = tk.Label(frame_details_client_4, text="Email", font='Helvetica 12 bold', anchor='w')
        email_label.pack(padx=5, pady=5, fill='both')
        email_entry = tk.Entry(frame_details_client_5, font="Helvetica 12", textvariable=self.email)
        self.email.set(self.data.get("client_email"))
        email_entry.config(state='readonly')
        email_entry.pack(padx=5, pady=5, fill='both')

        phone_1_label = tk.Label(frame_details_client_2, text="Telefono fijo", font='Helvetica 12 bold', anchor='w')
        phone_1_label.pack(padx=5, pady=5, fill='both')
        phone_1_entry = tk.Entry(frame_details_client_3, font="Helvetica 12", textvariable=self.phone_1)
        self.phone_1.set(self.data.get("client_phone_1"))
        phone_1_entry.config(state='readonly')
        phone_1_entry.pack(padx=5, pady=5, fill='both')

        phone_2_label = tk.Label(frame_details_client_4, text="Celular", font='Helvetica 12 bold', anchor='w')
        phone_2_label.pack(padx=5, pady=5, fill='both')
        phone_2_entry = tk.Entry(frame_details_client_5, font="Helvetica 12", textvariable=self.phone_2)
        self.phone_2.set(self.data.get("client_phone_2"))
        phone_2_entry.config(state='readonly')
        phone_2_entry.pack(padx=5, pady=5, fill='both')

        address_label = tk.Label(frame_details_client_7, text="Direccion", font='Helvetica 12 bold', anchor='w')
        address_label.pack(padx=5, pady=5, fill='both')
        address_entry = tk.Entry(frame_details_client_8, font="Helvetica 12", textvariable=self.address)
        self.address.set(self.data.get("client_address"))
        address_entry.config(state='readonly')
        address_entry.pack(padx=5, pady=5, fill='both')

        # Frame Vehicle details
        frame_details_vehicle = tk.LabelFrame(self.root, text="Datos del vehiculo", font='Helvetica 12 bold')
        frame_details_vehicle.pack(side="top", padx=5, pady=5, fill='x')

        frame_details_vehicle_1 = tk.Frame(frame_details_vehicle)
        frame_details_vehicle_1.pack(side="left", fill='both', padx=5, pady=5, expand=True)

        frame_details_vehicle_2 = tk.Frame(frame_details_vehicle)
        frame_details_vehicle_2.pack(side="left", fill='both', padx=5, pady=5, expand=True)

        frame_details_vehicle_3 = tk.Frame(frame_details_vehicle)
        frame_details_vehicle_3.pack(side="left", fill='both', padx=5, pady=5, expand=True)

        frame_details_vehicle_4 = tk.Frame(frame_details_vehicle)
        frame_details_vehicle_4.pack(side="left", fill='both', padx=5, pady=5, expand=True)

        vehicle_identity_label = tk.Label(frame_details_vehicle_1, text="Placa", font='Helvetica 12 bold', anchor='w')
        vehicle_identity_label.pack(padx=5, pady=5, fill='both')
        vehicle_identity_entry = tk.Entry(frame_details_vehicle_2, font="Helvetica 12", textvariable=self.vehicle_identity)
        self.vehicle_identity.set(self.data.get("vehicle_identity"))
        vehicle_identity_entry.config(state='readonly')
        vehicle_identity_entry.pack(padx=5, pady=5, fill='both')

        color_label = tk.Label(frame_details_vehicle_3, text="Color", font='Helvetica 12 bold', anchor='w')
        color_label.pack(padx=5, pady=5, fill='both')
        color_entry = tk.Entry(frame_details_vehicle_4, font="Helvetica 12", textvariable=self.color)
        self.color.set(self.data.get("vehicle_color"))
        color_entry.config(state='readonly')
        color_entry.pack(padx=5, pady=5, fill='both')

        vehicle_type_label = tk.Label(frame_details_vehicle_1, text="Tipo de Vehiculo", font='Helvetica 12 bold',
                                      anchor='w')
        vehicle_type_label.pack(padx=5, pady=5, fill='both')

        brand_entry = tk.Entry(frame_details_vehicle_2, font="Helvetica 12", textvariable=self.brand)
        self.brand.set(self.data.get("vehicle_type_brand"))
        brand_entry.config(state='readonly')
        brand_entry.pack(padx=5, pady=5, fill='both')

        model_entry = tk.Entry(frame_details_vehicle_3, font="Helvetica 12", textvariable=self.model)
        self.model.set(self.data.get("vehicle_type_model"))
        model_entry.config(state='readonly')
        model_entry.pack(padx=5, pady=5, fill='both')

        year_entry = tk.Entry(frame_details_vehicle_4, font="Helvetica 12", textvariable=self.year)
        self.year.set(self.data.get("vehicle_type_year"))
        year_entry.config(state='readonly')
        year_entry.pack(padx=5, pady=5, fill='both')

        mileage_label = tk.Label(frame_details_vehicle_1, text="Kilometraje", font='Helvetica 12 bold', anchor='w')
        mileage_label.pack(padx=5, pady=5, fill='both')
        mileage_entry = tk.Entry(frame_details_vehicle_2, font="Helvetica 12", textvariable=self.mileage)
        self.mileage.set(self.data.get("mileage"))
        mileage_entry.pack(padx=5, pady=5, fill='both')

        # Repair details
        frame_details_repair = tk.LabelFrame(self.root, text="Detalles de la Reparacion", font='Helvetica 12 bold')
        frame_details_repair.pack(side="top", padx=5, pady=5, fill='both')

        frame_details_repair_1 = tk.Frame(frame_details_repair)
        frame_details_repair_1.pack(side="top", fill='x', expand=True)

        frame_details_repair_1_a = tk.Frame(frame_details_repair_1)
        frame_details_repair_1_a.pack(side="left", padx=5, pady=5, fill='x', expand=True)
        frame_details_repair_1_a_a = tk.Frame(frame_details_repair_1_a)
        frame_details_repair_1_a_a.pack(side="top", fill='x', expand=True)

        frame_details_repair_1_b = tk.Frame(frame_details_repair_1)
        frame_details_repair_1_b.pack(side="left", fill='x', expand=True)
        frame_details_repair_1_b_a = tk.Frame(frame_details_repair_1_b)
        frame_details_repair_1_b_a.pack(side="top", fill='x', expand=True)

        frame_details_repair_2 = tk.Frame(frame_details_repair)
        frame_details_repair_2.pack(side="top", fill='x', expand=True)

        frame_details_repair_2_a = tk.Frame(frame_details_repair_2)
        frame_details_repair_2_a.pack(side="left", fill='x', expand=True)
        frame_details_repair_2_a_a = tk.Frame(frame_details_repair_2_a)
        frame_details_repair_2_a_a.pack(side="top", padx=5, pady=5, fill='x', expand=True)

        frame_details_repair_2_b = tk.Frame(frame_details_repair_2)
        frame_details_repair_2_b.pack(side="left", fill='x', expand=True)
        frame_details_repair_2_b_a = tk.Frame(frame_details_repair_2_b)
        frame_details_repair_2_b_a.pack(side="top", fill='x', expand=True)

        frame_details_repair_3 = tk.Frame(frame_details_repair)
        frame_details_repair_3.pack(side="top", fill='x', expand=True)

        frame_details_repair_3_a = tk.Frame(frame_details_repair_3)
        frame_details_repair_3_a.pack(side="left", padx=5, pady=5, fill='x', expand=True)

        # Date Entry
        date_entry_label = tk.Label(frame_details_repair_1_a_a, text="Fecha de entrada:", font='Helvetica 12 bold', anchor='w')
        date_entry_label.pack(side="left", padx=5, pady=5, fill='x')
        date_entry = DateEntry(frame_details_repair_1_a_a, width=10, background='darkblue', foreground='white', borderwidth=1, date_pattern='dd/mm/y', font='Helvetica 12 bold',textvariable=self.date_entry)
        self.date_entry.set(self.data.get("date_entry"))
        date_entry.pack(side="left", padx=5, pady=5, fill='x')

        # Client observations
        client_obs_label = tk.Label(frame_details_repair_1_a, text="Observaciones del Cliente:",
                                    font='Helvetica 12 bold', anchor='w')
        client_obs_label.pack(side="top", fill='x', expand=True)
        self.client_obs = tk.Text(frame_details_repair_1_a, height=4)
        self.client_obs.pack(side="left", fill="x", expand=True)
        self.client_obs.insert(tk.END, self.data.get("client_observations"))
        scrollbar_client = tk.Scrollbar(frame_details_repair_1_a)
        scrollbar_client.pack(side="left", fill="y")
        scrollbar_client.config(command=self.client_obs.yview)
        self.client_obs.config(yscrollcommand=scrollbar_client.set)

        # Date Exit
        date_exit_label = tk.Label(frame_details_repair_1_b_a, text="Fecha de salida:", font='Helvetica 12 bold',
                                   anchor='w')
        date_exit_label.pack(side="left", padx=5, pady=5, fill='x')
        date_exit = DateEntry(frame_details_repair_1_b_a, width=10, background='darkblue', foreground='white',
                              borderwidth=1,
                              date_pattern='dd/mm/y', font='Helvetica 12 bold', textvariable=self.date_exit)
        self.date_exit.set(self.data.get("date_exit"))
        date_exit.pack(side="left", padx=5, pady=5, fill='x')

        # Mechanical observations
        mechanical_obs_label = tk.Label(frame_details_repair_1_b, text="Observaciones del Mecanico:",
                                        font='Helvetica 12 bold', anchor='w')
        mechanical_obs_label.pack(side="top", fill='x', expand=True)
        scrollbar_mechanical = tk.Scrollbar(frame_details_repair_1_b)
        self.mechanical_obs = tk.Text(frame_details_repair_1_b, height=4)
        self.mechanical_obs.pack(side="left", fill="x", expand=True)
        self.mechanical_obs.insert(tk.END, self.data.get("mechanical_observations"))
        scrollbar_mechanical.pack(side="left", fill="y")
        scrollbar_mechanical.config(command=self.mechanical_obs.yview)
        self.mechanical_obs.config(yscrollcommand=scrollbar_mechanical.set)

        # Status
        status_label = tk.Label(frame_details_repair_2_a_a, text="Estado:", font='Helvetica 12 bold', anchor='w')
        status_label.pack(side="left", padx=5, pady=5, fill='x')
        self.status_chosen = ttk.Combobox(frame_details_repair_2_a_a, width=12, font='Helvetica 12 bold',
                                          state="readonly", textvariable=self.status_selected)
        self.status_selected.set(self.data.get("status"))
        self.status_chosen["values"] = ["EN TALLER", "FINALIZADO"]
        self.status_chosen.pack(side="left", padx=5, pady=5, fill='x')

        # Price
        price_label = tk.Label(frame_details_repair_2_b_a, text="Precio:", font='Helvetica 12 bold')
        price_label.pack(side="left", padx=5, pady=5)
        price_entry = tk.Entry(frame_details_repair_2_b_a, font="Helvetica 12 bold", textvariable=self.price)
        self.price.set(self.data.get("price"))
        price_entry.pack(side="left", padx=5, pady=5, fill='x', expand=True)

        # Final observations
        final_obs_label = tk.Label(frame_details_repair_3_a, text="Observacion final:", font='Helvetica 12 bold',
                                   anchor='w')
        final_obs_label.pack(side="top", fill='x', expand=True)
        self.final_obs = tk.Text(frame_details_repair_3_a, height=3)
        self.final_obs.insert(tk.END, self.data.get("final_observations"))
        self.final_obs.pack(side="left", fill="x", expand=True)
        scrollbar_final = tk.Scrollbar(frame_details_repair_3_a)
        scrollbar_final.pack(side="left", fill="y")
        scrollbar_final.config(command=self.client_obs.yview)
        self.final_obs.config(yscrollcommand=scrollbar_client.set)

        # Buttons
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(side="bottom", fill='x')

        button_1 = tk.Button(frame_buttons, text="Guardar", font='Helvetica 12 bold', width=15,
                             command=self.update_repair)
        button_1.pack(side='right', fil='x', padx=5, pady=5)

        button_2 = tk.Button(frame_buttons, text="Regresar", font='Helvetica 12 bold', width=15, command=self.go_back)
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

    def update_repair(self):
        """Update repair."""
        repair_data = {
            "vehicle_id": self.data.get("vehicle_id"),
            "mileage": self.mileage.get(),
            "client_observations": self.client_obs.get("1.0", "end"),
            "mechanical_observations": self.mechanical_obs.get("1.0", "end"),
            "final_observations": self.final_obs.get("1.0", "end"),
            "date_entry": self.date_entry.get(),
            "date_exit": self.date_exit.get(),
            "price": self.price.get(),
            "status": self.status_selected.get()
        }

        repair = self.repair.update(repair_id=self.repair_id, data=repair_data)
        if repair:
            self.show_info(message="La reparacion ha sido registrada exitosamente.")
        else:
            self.show_error(message="ERROR: La reparacion no ha sido creada.")
