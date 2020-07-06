import tkinter as tk
from tkinter import ttk

from backend.exceptions.vehicle_exceptions import VehicleUpdateException
from graphic_interface.menus.base_frame import BaseFrame


class FormEditVehicle(BaseFrame):
    """Class for Form Edit Vehicle window."""

    def __init__(self, root, connection, master, values):
        """FormEditVehicle init."""
        super().__init__(root=root, connection=connection)
        self.master = master
        self.root['bg'] = 'black'
        # Get Client details
        client_id = int(values[6])
        client = self.client.get_by_id(client_id=client_id)
        self._client = tk.StringVar()
        self.client_id = tk.StringVar()
        self.client_id.set(values[6])
        self.name = tk.StringVar()
        self.last_name = tk.StringVar()
        self.identity_card = tk.StringVar()
        self.email = tk.StringVar()
        self.phone_1 = tk.StringVar()
        self.phone_2 = tk.StringVar()
        self.address = tk.StringVar()

        #Get Vehicle details
        self.vehicle_id = values[0]
        self.identity = tk.StringVar()
        self.color = tk.StringVar()

        # Get Vehicle type details
        self.vehicle_type_id = tk.StringVar()
        self.brand = tk.StringVar()
        self.model = tk.StringVar()
        self.year = tk.StringVar()

        # Frame Search clients
        frame = tk.LabelFrame(self.root, text="Buscar cliente", bg="black", foreground="white", font='bold')
        frame.pack(side="top", padx=5, pady=5, fill='x')

        # Frame Details Clients
        frame_1 = tk.LabelFrame(self.root, text="Datos del cliente", bg="black", foreground="white", font='bold')
        frame_1.pack(side="top", padx=5, pady=5, fill='x')

        frame_2 = tk.Frame(frame_1, bg="black")
        frame_2.pack(side="top", padx=5, pady=5, fill='x')

        frame_3 = tk.Frame(frame_2, bg="black")
        frame_3.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_4 = tk.Frame(frame_2, bg="black")
        frame_4.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_5 = tk.Frame(frame_2, bg="black")
        frame_5.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_6 = tk.Frame(frame_2, bg="black")
        frame_6.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_7 = tk.Frame(frame_1, bg="black")
        frame_7.pack(side="top", padx=5, pady=5, fill='x')

        frame_8 = tk.Frame(frame_7, bg="black")
        frame_8.pack(side="left", fill='x')

        frame_9 = tk.Frame(frame_7, bg="black")
        frame_9.pack(side="left", fill='x', expand=True)

        # Frame Vehicle
        frame_10 = tk.LabelFrame(self.root, text="Inserte los datos del vehiculo", bg="black", foreground="white", font='bold')
        frame_10.pack(side="top", padx=5, pady=5, fill='x')

        frame_11 = tk.Frame(frame_10, bg="black")
        frame_11.pack(side="top", padx=5, pady=5, fill='x')

        frame_12 = tk.Frame(frame_11, bg="black")
        frame_12.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_13 = tk.Frame(frame_11, bg="black")
        frame_13.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_14 = tk.Frame(frame_11, bg="black")
        frame_14.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_15 = tk.Frame(frame_11, bg="black")
        frame_15.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        frame_16 = tk.Frame(frame_10, bg="black")
        frame_16.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        # Frame Buttons
        frame_17 = tk.Frame(self.root, bg="black")
        frame_17.pack(side="bottom", padx=5, pady=5, fill='x')

        # Choose Client
        self.client_chosen = ttk.Combobox(frame, width=20, font='Helvetica 18 bold', state="readonly", textvariable=self._client)
        self._client.set(self.get_client_by_id(client_id=values[6]))
        self._client.trace_add("write", self.callback_client)
        self.client_chosen["values"] = self.get_clients()
        self.client_chosen.pack(side="top", padx=5, pady=5, fill='x', expand=True)

        # Client Data
        name_label = tk.Label(frame_3, text="Nombre", font='Helvetica 18 bold', anchor='w', foreground="gold2", bg= "black")
        name_label.pack(padx=5, pady=5, fill='both')
        name_entry = tk.Entry(frame_4, font="Helvetica 17", textvariable=self.name)
        self.name.set(client[0].get("name"))
        name_entry.config(state='readonly')
        name_entry.pack(padx=5, pady=5, fill='both')

        last_name_label = tk.Label(frame_5, text="Apellido", font='Helvetica 18 bold', anchor='w', foreground="gold2", bg= "black")
        last_name_label.pack(padx=5, pady=5, fill='both')
        last_name_entry = tk.Entry(frame_6, font="Helvetica 17", textvariable=self.last_name)
        self.last_name.set(client[0].get("last_name"))
        last_name_entry.config(state='readonly')
        last_name_entry.pack(padx=5, pady=5, fill='both')

        identity_card_label = tk.Label(frame_3, text="Cedula", font='Helvetica 18 bold', anchor='w', foreground="gold2", bg= "black")
        identity_card_label.pack(padx=5, pady=5, fill='both')
        identity_card_entry = tk.Entry(frame_4, font="Helvetica 17", textvariable=self.identity_card)
        self.identity_card.set(client[0].get("identity_card"))
        identity_card_entry.config(state='readonly')
        identity_card_entry.pack(padx=5, pady=5, fill='both')

        email_label = tk.Label(frame_5, text="Email", font='Helvetica 18 bold', anchor='w', foreground="gold2", bg= "black")
        email_label.pack(padx=5, pady=5, fill='both')
        email_entry = tk.Entry(frame_6, font="Helvetica 17", textvariable=self.email)
        self.email.set(client[0].get("email"))
        email_entry.config(state='readonly')
        email_entry.pack(padx=5, pady=5, fill='both')

        phone_1_label = tk.Label(frame_3, text="Telefono fijo", font='Helvetica 18 bold', anchor='w', foreground="gold2", bg= "black")
        phone_1_label.pack(padx=5, pady=5, fill='both')
        phone_1_entry = tk.Entry(frame_4, font="Helvetica 17", textvariable=self.phone_1)
        self.phone_1.set(client[0].get("phone_1"))
        phone_1_entry.config(state='readonly')
        phone_1_entry.pack(padx=5, pady=5, fill='both')

        phone_2_label = tk.Label(frame_5, text="Celular", font='Helvetica 18 bold', anchor='w', foreground="gold2", bg= "black")
        phone_2_label.pack(padx=5, pady=5, fill='both')
        phone_2_entry = tk.Entry(frame_6, font="Helvetica 17", textvariable=self.phone_2)
        self.phone_2.set(client[0].get("phone_2"))
        phone_2_entry.config(state='readonly')
        phone_2_entry.pack(padx=5, pady=5, fill='both')

        address_label = tk.Label(frame_8, text="Direccion", font='Helvetica 18 bold', anchor='w', foreground="gold2", bg= "black")
        address_label.pack(padx=5, pady=5, fill='both')
        address_entry = tk.Entry(frame_9, font="Helvetica 17", textvariable=self.address)
        self.address.set(client[0].get("address"))
        address_entry.config(state='readonly')
        address_entry.pack(padx=5, pady=5, fill='both')

        # Vehicle Data
        identity_label = tk.Label(frame_12, text="Placa", font='Helvetica 18 bold', anchor='w', foreground="gold2", bg= "black")
        identity_label.pack(padx=5, pady=5, fill='both')
        identity_entry = tk.Entry(frame_13, font="Helvetica 17", textvariable=self.identity)
        self.identity.set(values[1])
        identity_entry.pack(padx=5, pady=5, fill='both')

        color_label = tk.Label(frame_14, text="Color", font='Helvetica 18 bold', anchor='w', foreground="gold2", bg= "black")
        color_label.pack(padx=5, pady=5, fill='both')
        color_entry = tk.Entry(frame_15, font="Helvetica 17", textvariable=self.color)
        self.color.set(values[2])
        color_entry.pack(padx=5, pady=5, fill='both')

        number_label = tk.Label(frame_16, text="Tipo de Vehiculo", font='Helvetica 18 bold', anchor='w', foreground="gold2", bg= "black")
        number_label.pack(side='left', padx=5, pady=5, fill='both')

        self.brand_chosen = ttk.Combobox(frame_16, width=20, font='Helvetica 18 bold', textvariable=self.brand, state="readonly")
        self.brand.set(values[4])
        self.brand_chosen["values"] = self.get_vehicle_type_brands()
        self.brand_chosen.pack(side='left', padx=5, pady=5, expand=True)

        self.model_chosen = ttk.Combobox(frame_16, width=20, font='Helvetica 18 bold', textvariable=self.model, state="readonly")
        self.model.set(values[3])
        self.model_chosen.pack(side='left', padx=5, pady=5, expand=True)
        # Choose Vehicle type (Brand, Model, Year).
        self.brand.trace_add("write", self.callback_vehicle_type)
        self.model.trace_add("write", self.callback_vehicle_type)

        self.year_chosen = ttk.Combobox(frame_16, width=20, font='Helvetica 18 bold', textvariable=self.year, state="readonly")
        self.year.set(values[5])
        self.year_chosen.pack(side='left', padx=5, pady=5, expand=True)


        # Buttons
        button_1 = tk.Button(frame_17, text="Guardar", font='Helvetica 15 bold', width=15, bg="gold2", command=self.edit_vehicle)
        button_1.pack(side='right', fil='x')

        button_2 = tk.Button(frame_17, text="Regresar", font='Helvetica 15 bold', width=15, bg="gold2", command=self.go_back)
        button_2.pack(side='right', fil='x')

        self.root.mainloop()

    def edit_vehicle(self):
        """Edit vehicle."""
        vehicle_type_id = self.vehicle_type.get_vehicle_type_id(
            brand=self.brand.get(),
            model=self.model.get(),
            year=int(self.year.get())
        )
        client_id = self.client_id.get()
        vehicle_type_id = vehicle_type_id
        identity = self.identity.get()
        color = self.color.get()

        try:
            self.vehicle.update(
                vehicle_id=self.vehicle_id,
                client_id=client_id,
                vehicle_type_id=vehicle_type_id,
                identity=identity,
                color=color
            )
        except VehicleUpdateException:
            self.show_error(message="ERROR: El vehiculo no ha podido ser actualizado.")
            raise VehicleUpdateException()
        self.show_info(message=f"Los datos del vehiculo han sido actualizados exitosamente.")

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

    def callback_vehicle_type(self, *args):
        brand = self.brand.get()
        model = self.model.get()
        self.model_chosen.config(values=self.get_vehicle_type_models(brand=brand))
        self.year_chosen.config(values=self.get_vehicle_type_year(model=model))

    def callback_client(self, *args):
        self.client_chosen["values"] = self.get_clients()
        client = self._client.get()
        list = client.split(' ')
        client = self.client.get_by_id(client_id=list[0])[0]
        self.client_id.set(client.get("client_id")),
        self.name.set(client.get("name"))
        self.last_name.set(client.get("last_name"))
        self.identity_card.set(client.get("identity_card"))
        self.email.set(client.get("email"))
        self.phone_1.set(client.get("phone_1"))
        self.phone_2.set(client.get("phone_2"))
        self.address.set(client.get("address"))

    def go_back(self):
        """Go back to Menu Client."""
        self.hide()
        self.master.show()

    def get_clients(self):
        """Get clients."""
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

    def get_client_by_id(self, client_id:str):
        """Get client by id."""
        clients = self.get_clients()
        for client in clients:
            if client[0] == client_id:
                return client
