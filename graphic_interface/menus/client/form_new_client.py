import tkinter as tk

from database.database import Database
from graphic_interface.menus.base_frame import BaseFrame
from settings import DATABASE

from core.client import Client

database = Database(database=DATABASE)
connection = database.get_connection()
client = Client(connection=connection)
# Create tables


class FormNewClient(BaseFrame):
    """Class FormNewClient."""

    def __init__(self, root, connection, master):
        """FormNewClient init."""
        super().__init__(root=root, connection=connection)
        self.root.title('Taller Mecanico Echenique - Programa de gestion')
        self.root.state('zoomed')
        self.master = master
        self.data = {
            "name": tk.StringVar(),
            "last_name": tk.StringVar(),
            "identity_card": tk.StringVar(),
            "email": tk.StringVar(),
            "phone_1": tk.StringVar(),
            "phone_2": tk.StringVar(),
            "address": tk.StringVar()
        }

        buttons_frame = tk.LabelFrame(self.root, text="Nuevo cliente")
        buttons_frame.pack(side="left",padx=5, pady=5, fill='both', expand=True)

        buttons_frame_1 = tk.Frame(buttons_frame)
        buttons_frame_1.pack(side="top", padx=5, pady=5, fill='x')

        buttons_frame_2 = tk.Frame(buttons_frame_1)
        buttons_frame_2.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        buttons_frame_3 = tk.Frame(buttons_frame_1)
        buttons_frame_3.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        buttons_frame_4 = tk.Frame(buttons_frame_1)
        buttons_frame_4.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        buttons_frame_5 = tk.Frame(buttons_frame_1)
        buttons_frame_5.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        buttons_frame_6 = tk.Frame(buttons_frame)
        buttons_frame_6.pack(side="top", padx=5, pady=5, fill='x')

        buttons_frame_7 = tk.Frame(buttons_frame_6)
        buttons_frame_7.pack(side="left", fill='x')

        buttons_frame_8 = tk.Frame(buttons_frame_6)
        buttons_frame_8.pack(side="left",fill='x', expand=True)

        buttons_frame_9 = tk.Frame(buttons_frame)
        buttons_frame_9.pack(side="bottom", padx=5, pady=5, fill='x')

        name_label = tk.Label(buttons_frame_2, text="Nombre", font='Helvetica 18 bold', anchor='w')
        name_label.pack(padx=5, pady=5, fill='both')
        name_entry = tk.Entry(buttons_frame_3, font = "Helvetica 17", textvariable=self.data["name"])
        name_entry.pack(padx=5, pady=5, fill='both')

        last_name_label = tk.Label(buttons_frame_4, text="Apellido", font='Helvetica 18 bold', anchor='w')
        last_name_label.pack(padx=5, pady=5, fill='both')
        last_name_entry = tk.Entry(buttons_frame_5, font = "Helvetica 17", textvariable=self.data["last_name"])
        last_name_entry.pack(padx=5, pady=5, fill='both')

        identity_card_label = tk.Label(buttons_frame_2, text="Cedula", font='Helvetica 18 bold', anchor='w')
        identity_card_label.pack(padx=5, pady=5, fill='both')
        identity_card_entry = tk.Entry(buttons_frame_3, font="Helvetica 17", textvariable=self.data["identity_card"])
        identity_card_entry.pack(padx=5, pady=5, fill='both')

        email_label = tk.Label(buttons_frame_4, text="Email", font='Helvetica 18 bold', anchor='w')
        email_label.pack(padx=5, pady=5, fill='both')
        email_entry = tk.Entry(buttons_frame_5, font="Helvetica 17", textvariable=self.data["email"])
        email_entry.pack(padx=5, pady=5, fill='both')

        phone_1_label = tk.Label(buttons_frame_2, text="Telefono fijo", font='Helvetica 18 bold', anchor='w')
        phone_1_label.pack(padx=5, pady=5, fill='both')
        phone_1_entry = tk.Entry(buttons_frame_3, font="Helvetica 17", textvariable=self.data["phone_1"])
        phone_1_entry.pack(padx=5, pady=5, fill='both')

        phone_2_label = tk.Label(buttons_frame_4, text="Celular", font='Helvetica 18 bold', anchor='w')
        phone_2_label.pack(padx=5, pady=5, fill='both')
        phone_2_entry = tk.Entry(buttons_frame_5, font="Helvetica 17", textvariable=self.data["phone_2"])
        phone_2_entry.pack(padx=5, pady=5, fill='both')

        address_label = tk.Label(buttons_frame_7, text="Direccion", font='Helvetica 18 bold', anchor='w')
        address_label.pack(padx=5, pady=5, fill='both')
        address_entry = tk.Entry(buttons_frame_8, font="Helvetica 17", textvariable=self.data["address"])
        address_entry.pack(padx=5, pady=5, fill='both')

        buttonW = tk.Button(buttons_frame_9, text="Crear", font='Helvetica 15 bold', width=15, command=self.insert_data)
        buttonW.pack(side='right', fil='x')

        buttonE = tk.Button(buttons_frame_9, text="Regresar", font='Helvetica 15 bold', width=15, command=self.go_back)
        buttonE.pack(side='right', fil='x')

        self.root.mainloop()

    def insert_data(self):
        data = {
            "name": self.data["name"].get(),
            "last_name": self.data["last_name"].get(),
            "identity_card": self.data["identity_card"].get(),
            "email": self.data["email"].get(),
            "phone_1": self.data["phone_1"].get(),
            "phone_2": self.data["phone_2"].get(),
            "address": self.data["address"].get()
        }
        self.create_client(data=data)

    def go_back(self):
        self.hide()
        self.master.show()

