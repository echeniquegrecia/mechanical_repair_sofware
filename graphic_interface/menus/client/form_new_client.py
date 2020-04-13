import tkinter as tk

from graphic_interface.menus.base_frame import BaseFrame

class FormNewClient(BaseFrame):
    """Class for New Client Window."""

    def __init__(self, root, connection, master):
        """New Client Window init."""
        super().__init__(root=root, connection=connection)
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

        frame_1 = tk.LabelFrame(self.root, text="Nuevo cliente")
        frame_1.pack(side="left",padx=5, pady=5, fill='both', expand=True)

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
        frame_9.pack(side="left",fill='x', expand=True)

        frame_10 = tk.Frame(frame_1)
        frame_10.pack(side="bottom", padx=5, pady=5, fill='x')

        name_label = tk.Label(frame_3, text="Nombre", font='Helvetica 18 bold', anchor='w')
        name_label.pack(padx=5, pady=5, fill='both')
        name_entry = tk.Entry(frame_4, font = "Helvetica 17", textvariable=self.data["name"])
        name_entry.pack(padx=5, pady=5, fill='both')

        last_name_label = tk.Label(frame_5, text="Apellido", font='Helvetica 18 bold', anchor='w')
        last_name_label.pack(padx=5, pady=5, fill='both')
        last_name_entry = tk.Entry(frame_6, font = "Helvetica 17", textvariable=self.data["last_name"])
        last_name_entry.pack(padx=5, pady=5, fill='both')

        identity_card_label = tk.Label(frame_3, text="Cedula", font='Helvetica 18 bold', anchor='w')
        identity_card_label.pack(padx=5, pady=5, fill='both')
        identity_card_entry = tk.Entry(frame_4, font="Helvetica 17", textvariable=self.data["identity_card"])
        identity_card_entry.pack(padx=5, pady=5, fill='both')

        email_label = tk.Label(frame_5, text="Email", font='Helvetica 18 bold', anchor='w')
        email_label.pack(padx=5, pady=5, fill='both')
        email_entry = tk.Entry(frame_6, font="Helvetica 17", textvariable=self.data["email"])
        email_entry.pack(padx=5, pady=5, fill='both')

        phone_1_label = tk.Label(frame_3, text="Telefono fijo", font='Helvetica 18 bold', anchor='w')
        phone_1_label.pack(padx=5, pady=5, fill='both')
        phone_1_entry = tk.Entry(frame_4, font="Helvetica 17", textvariable=self.data["phone_1"])
        phone_1_entry.pack(padx=5, pady=5, fill='both')

        phone_2_label = tk.Label(frame_5, text="Celular", font='Helvetica 18 bold', anchor='w')
        phone_2_label.pack(padx=5, pady=5, fill='both')
        phone_2_entry = tk.Entry(frame_6, font="Helvetica 17", textvariable=self.data["phone_2"])
        phone_2_entry.pack(padx=5, pady=5, fill='both')

        address_label = tk.Label(frame_8, text="Direccion", font='Helvetica 18 bold', anchor='w')
        address_label.pack(padx=5, pady=5, fill='both')
        address_entry = tk.Entry(frame_9, font="Helvetica 17", textvariable=self.data["address"])
        address_entry.pack(padx=5, pady=5, fill='both')

        button_1 = tk.Button(frame_10, text="Crear", font='Helvetica 15 bold', width=15, command=self.create_new_client)
        button_1.pack(side='right', fil='x')

        button_2 = tk.Button(frame_10, text="Regresar", font='Helvetica 15 bold', width=15, command=self.go_back)
        button_2.pack(side='right', fil='x')

        self.root.mainloop()

    def create_new_client(self):
        """Create new client."""
        data = {
            "name": self.data["name"].get(),
            "last_name": self.data["last_name"].get(),
            "identity_card": self.data["identity_card"].get(),
            "email": self.data["email"].get(),
            "phone_1": self.data["phone_1"].get(),
            "phone_2": self.data["phone_2"].get(),
            "address": self.data["address"].get()
        }
        result = self.client.create(data=data)
        if result:
            self.show_info(message="El cliente ha sido registrado exitosamente")
        else:
            self.show_info(message="ERROR: El cliente no ha sido creado.")

    def go_back(self):
        """Go back to Menu Client."""
        self.hide()
        self.master.show()
