import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

from backend.exceptions.repair_exceptions import RepairCreateException
from graphic_interface.menus.base_frame import BaseFrame

class FormNewRepair(BaseFrame):
    """Class for Form New Repair window."""

    def __init__(self, root, connection, master):
        """FormNewRepair init."""
        super().__init__(root=root, connection=connection)
        self.root.state('zoomed')
        self.master = master
        self.client_selected = tk.StringVar()
        self.vehicle_selected = tk.StringVar()
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
        self.status_selected = tk.StringVar()
        self.mileage = tk.StringVar()
        self.client_obs = tk.StringVar()
        self.mechanical_obs = tk.StringVar()
        self.final_obs = tk.StringVar()
        self.price = tk.StringVar()
        self.date_entry = tk.StringVar()
        self.date_exit = tk.StringVar()

        # Frame Search clients
        frame_search_client = tk.LabelFrame(self.root, text="Buscar cliente", font='Helvetica 12 bold')
        frame_search_client.pack(side="top", padx=5, pady=5, fill='x')

        self.client_selected.trace_add("write", self.callback_client)
        self.client_chosen = ttk.Combobox(frame_search_client, width=20, font='Helvetica 12 bold', state="readonly",textvariable=self.client_selected)
        self.client_chosen["values"] = self.get_clients()
        self.client_chosen.pack(side="top", padx=5, pady=5, fill='x', expand=True)

        # Frame Details Clients
        frame_details_client = tk.LabelFrame(self.root, text="Datos del cliente", font='Helvetica 12 bold')
        frame_details_client.pack(side="top", padx=5, pady=5, fill='x')

        frame_details_client_1 = tk.Frame(frame_details_client)
        frame_details_client_1.pack(side="top", fill='x')

        frame_details_client_2 = tk.Frame(frame_details_client_1)
        frame_details_client_2.pack(side="left", fill='x',  expand=True)

        frame_details_client_3 = tk.Frame(frame_details_client_1)
        frame_details_client_3.pack(side="left", fill='x',  expand=True)

        frame_details_client_4 = tk.Frame(frame_details_client_1)
        frame_details_client_4.pack(side="left", fill='x',  expand=True)

        frame_details_client_5 = tk.Frame(frame_details_client_1)
        frame_details_client_5.pack(side="left", fill='x',  expand=True)

        frame_details_client_6 = tk.Frame(frame_details_client)
        frame_details_client_6.pack(side="top",  fill='x')

        frame_details_client_7 = tk.Frame(frame_details_client_6)
        frame_details_client_7.pack(side="left", fill='x')

        frame_details_client_8 = tk.Frame(frame_details_client_6)
        frame_details_client_8.pack(side="left", fill='x', expand=True)

        name_label = tk.Label(frame_details_client_2, text="Nombre", font='Helvetica 12 bold', anchor='w')
        name_label.pack(padx=5, pady=5, fill='both')
        name_entry = tk.Entry(frame_details_client_3, font="Helvetica 12", textvariable=self.name)
        name_entry.config(state='readonly')
        name_entry.pack(padx=5, pady=5, fill='both')

        last_name_label = tk.Label(frame_details_client_4, text="Apellido", font='Helvetica 12 bold', anchor='w')
        last_name_label.pack(padx=5, pady=5, fill='both')
        last_name_entry = tk.Entry(frame_details_client_5, font="Helvetica 12", textvariable=self.last_name)
        last_name_entry.config(state='readonly')
        last_name_entry.pack(padx=5, pady=5, fill='both')

        identity_card_label = tk.Label(frame_details_client_2, text="Cedula", font='Helvetica 12 bold', anchor='w')
        identity_card_label.pack(padx=5, pady=5, fill='both')
        identity_card_entry = tk.Entry(frame_details_client_3, font="Helvetica 12", textvariable=self.identity_card)
        identity_card_entry.config(state='readonly')
        identity_card_entry.pack(padx=5, pady=5, fill='both')

        email_label = tk.Label(frame_details_client_4, text="Email", font='Helvetica 12 bold', anchor='w')
        email_label.pack(padx=5, pady=5, fill='both')
        email_entry = tk.Entry(frame_details_client_5, font="Helvetica 12", textvariable=self.email)
        email_entry.config(state='readonly')
        email_entry.pack(padx=5, pady=5, fill='both')

        phone_1_label = tk.Label(frame_details_client_2, text="Telefono fijo", font='Helvetica 12 bold', anchor='w')
        phone_1_label.pack(padx=5, pady=5, fill='both')
        phone_1_entry = tk.Entry(frame_details_client_3, font="Helvetica 12", textvariable=self.phone_1)
        phone_1_entry.config(state='readonly')
        phone_1_entry.pack(padx=5, pady=5, fill='both')

        phone_2_label = tk.Label(frame_details_client_4, text="Celular", font='Helvetica 12 bold', anchor='w')
        phone_2_label.pack(padx=5, pady=5, fill='both')
        phone_2_entry = tk.Entry(frame_details_client_5, font="Helvetica 12", textvariable=self.phone_2)
        phone_2_entry.config(state='readonly')
        phone_2_entry.pack(padx=5, pady=5, fill='both')

        address_label = tk.Label(frame_details_client_7, text="Direccion", font='Helvetica 12 bold', anchor='w')
        address_label.pack(padx=5, pady=5, fill='both')
        address_entry = tk.Entry(frame_details_client_8, font="Helvetica 12", textvariable=self.address)
        address_entry.config(state='readonly')
        address_entry.pack(padx=5, pady=5, fill='both')

        # Frame Search vehicle
        frame_search_vehicle = tk.LabelFrame(self.root, text="Buscar vehiculo", font='Helvetica 12 bold')
        frame_search_vehicle.pack(side="top", padx=5, pady=5, fill='x')

        self.vehicle_selected.trace_add("write", self.callback_vehicle)
        self.vehicle_chosen = ttk.Combobox(frame_search_vehicle, width=20, font='Helvetica 12 bold', state="readonly",textvariable=self.vehicle_selected)
        self.vehicle_chosen.pack(side="top", padx=5, pady=5, fill='x', expand=True)

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

        self.vehicle_identity.trace_add("write", self.callback_vehicle)
        self.color.trace_add("write", self.callback_vehicle)
        self.brand.trace_add("write", self.callback_vehicle)
        self.model.trace_add("write", self.callback_vehicle)
        self.year.trace_add("write", self.callback_vehicle)

        vehicle_identity_label = tk.Label(frame_details_vehicle_1, text="Placa", font='Helvetica 12 bold', anchor='w')
        vehicle_identity_label.pack(padx=5, pady=5, fill='both')
        vehicle_identity_entry = tk.Entry(frame_details_vehicle_2, font="Helvetica 12", textvariable=self.vehicle_identity)
        vehicle_identity_entry.config(state='readonly')
        vehicle_identity_entry.pack(padx=5, pady=5, fill='both')

        color_label = tk.Label(frame_details_vehicle_3, text="Color", font='Helvetica 12 bold', anchor='w')
        color_label.pack(padx=5, pady=5, fill='both')
        color_entry = tk.Entry(frame_details_vehicle_4, font="Helvetica 12", textvariable=self.color)
        color_entry.config(state='readonly')
        color_entry.pack(padx=5, pady=5, fill='both')

        vehicle_type_label = tk.Label(frame_details_vehicle_1, text="Tipo de Vehiculo", font='Helvetica 12 bold', anchor='w')
        vehicle_type_label.pack(padx=5, pady=5, fill='both')

        brand_entry = tk.Entry(frame_details_vehicle_2, font="Helvetica 12", textvariable=self.brand)
        brand_entry.config(state='readonly')
        brand_entry.pack(padx=5, pady=5, fill='both')

        model_entry = tk.Entry(frame_details_vehicle_3, font="Helvetica 12", textvariable=self.model)
        model_entry.config(state='readonly')
        model_entry.pack(padx=5, pady=5, fill='both')

        year_entry = tk.Entry(frame_details_vehicle_4, font="Helvetica 12", textvariable=self.year)
        year_entry.config(state='readonly')
        year_entry.pack(padx=5, pady=5, fill='both')

        mileage_label = tk.Label(frame_details_vehicle_1, text="Kilometraje", font='Helvetica 12 bold', anchor='w')
        mileage_label.pack(padx=5, pady=5, fill='both')
        mileage_entry = tk.Entry(frame_details_vehicle_2, font="Helvetica 12", textvariable=self.mileage)
        mileage_entry.pack(padx=5, pady=5, fill='both')

        # Repair details
        frame_details_repair = tk.LabelFrame(self.root, text="Detalles de la Reparacion", font='Helvetica 12 bold')
        frame_details_repair.pack(side="top", padx=5, pady=5, fill='both')

        frame_details_repair_1= tk.Frame(frame_details_repair)
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
        date_entry = DateEntry(frame_details_repair_1_a_a, width=10, background='darkblue', foreground='white', borderwidth=1,  date_pattern='dd/mm/y', font='Helvetica 12 bold', textvariable=self.date_entry)
        date_entry.pack(side="left", padx=5, pady=5, fill='x')

        # Client observations
        client_obs_label = tk.Label(frame_details_repair_1_a, text="Observaciones del Cliente:", font='Helvetica 12 bold', anchor='w')
        client_obs_label.pack(side="top", fill='x', expand=True)
        self.client_obs = tk.Text(frame_details_repair_1_a, height=4)
        self.client_obs.pack(side="left", fill="x", expand=True)
        scrollbar_client = tk.Scrollbar(frame_details_repair_1_a)
        scrollbar_client.pack(side="left", fill="y")
        scrollbar_client.config(command=self.client_obs.yview)
        self.client_obs.config(yscrollcommand=scrollbar_client.set)

        # Status
        status_label = tk.Label(frame_details_repair_2_a_a, text="Estado:", font='Helvetica 12 bold', anchor='w')
        status_label.pack(side="left", padx=5, pady=5, fill='x')
        self.status_chosen = ttk.Combobox(frame_details_repair_2_a_a, width=12, font='Helvetica 12 bold',
                                          state="readonly", textvariable=self.status_selected)
        self.status_chosen["values"] = ["EN TALLER"]
        self.status_chosen.current(0)
        self.status_chosen.pack(side="left", padx=5, pady=5, fill='x')

        # Date Exit
        date_exit_label = tk.Label(frame_details_repair_1_b_a, text="Fecha de salida:", font='Helvetica 12 bold',
                                   anchor='w')
        date_exit_label.pack(side="left", padx=5, pady=5, fill='x')
        date_exit = DateEntry(frame_details_repair_1_b_a, width=10, background='darkblue', foreground='white', borderwidth=1,
                              date_pattern='dd/mm/y', font='Helvetica 12 bold', textvariable=self.date_exit)
        date_exit.delete(0, "end")
        date_exit.config(state="disabled")
        date_exit.pack(side="left", padx=5, pady=5, fill='x')

        # Mechanical observations
        mechanical_obs_label = tk.Label(frame_details_repair_1_b, text="Observaciones del Mecanico:", font='Helvetica 12 bold', anchor='w')
        mechanical_obs_label.pack(side="top",  fill='x', expand=True)
        scrollbar_mechanical = tk.Scrollbar(frame_details_repair_1_b)
        self.mechanical_obs = tk.Text(frame_details_repair_1_b, height=4)
        self.mechanical_obs.pack(side="left", fill="x", expand=True)
        scrollbar_mechanical.pack(side="left", fill="y")
        scrollbar_mechanical.config(command=self.mechanical_obs.yview)
        self.mechanical_obs.config(yscrollcommand=scrollbar_mechanical.set)

        # Price
        price_label = tk.Label(frame_details_repair_2_b_a, text="Precio:", font='Helvetica 12 bold')
        price_label.pack(side="left", padx=5, pady=5)
        price_entry = tk.Entry(frame_details_repair_2_b_a, font="Helvetica 12 bold", textvariable=self.price)
        price_entry.pack(side="left", padx=5, pady=5, fill='x', expand=True)

        # Final observations
        final_obs_label = tk.Label(frame_details_repair_3_a, text="Observacion final:", font='Helvetica 12 bold', anchor='w')
        final_obs_label.pack(side="top",  fill='x', expand=True)
        self.final_obs = tk.Text(frame_details_repair_3_a, height=3)
        self.final_obs.configure(state='disabled')
        self.final_obs.pack(side="left", fill="x", expand=True)
        scrollbar_final = tk.Scrollbar(frame_details_repair_3_a)
        scrollbar_final.pack(side="left", fill="y")
        scrollbar_final.config(command=self.client_obs.yview)
        self.final_obs.config(yscrollcommand=scrollbar_client.set)

        # Buttons
        frame_buttons = tk.Frame(self.root)
        frame_buttons.pack(side="bottom", fill='x')

        button_1 = tk.Button(frame_buttons, text="Crear", font='Helvetica 12 bold', width=15, command=self.create_repair)
        button_1.pack(side='right', fil='x', padx=5, pady=5)

        button_2 = tk.Button(frame_buttons, text="Regresar", font='Helvetica 12 bold', width=15, command=self.go_back)
        button_2.pack(side='right', fil='x', padx=5, pady=5)

        self.root.mainloop()

    def callback_client(self, *args):
        client = self.client_selected.get()
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

    def callback_vehicle(self, *args):
        vehicle = self.vehicle_selected.get()
        vehicle_id = vehicle.split(' ')[0]
        self.vehicle_id.set(vehicle_id)
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

    def create_repair(self):
        """Create repair."""
        vehicle_id = self.vehicle_id.get()
        mileage = self.mileage.get()
        client_observations = self.client_obs.get("1.0", "end")
        mechanical_observations = self.mechanical_obs.get("1.0", "end")
        final_observations = self.final_obs.get("1.0", "end")
        date_entry = self.date_entry.get()
        date_exit = self.date_exit.get()
        price = self.price.get()
        status = self.status_selected.get()

        try:
            self.repair.create(
                vehicle_id=vehicle_id,
                mileage=mileage,
                client_observations=client_observations,
                mechanical_observations=mechanical_observations,
                final_observations=final_observations,
                date_entry=date_entry,
                date_exit=date_exit,
                price=price,
                status=status
            )
        except RepairCreateException as error:
            if error.message == "Date entry can not be newer than Date exit.":
                self.show_error(
                    message="ERROR: La fecha de entrada no puede ser mayor que la fecha de salida."
                )
            if error.message == "The status value is not in [EN TALLER, FINALIZADO]":
                self.show_error(
                    message="ERROR: El valor del estado no es correcto."
                )
            if error.message == "The mileage value is not correct":
                self.show_error(
                    message="ERROR: El valor del kilometraje no es correcto."
                )
            if error.message == "The price value is not correct":
                self.show_error(
                    message="ERROR: El valor del precio no es correcto."
                )
            self.show_error(message="ERROR: La reparacion no ha sido creada.")
            raise RepairCreateException()
        self.show_info(message="La reparacion ha sido registrada exitosamente.")
