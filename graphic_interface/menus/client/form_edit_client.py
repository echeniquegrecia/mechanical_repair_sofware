import tkinter as tk
from tkinter import ttk


from graphic_interface.menus.base_frame import BaseFrame


class FormEditClient(BaseFrame):
    """Class FormEditClient."""

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

        buttons_frame = tk.LabelFrame(self.root, text="Editar-Borrar Client", width=100, height=10)
        buttons_frame.pack(side='left', ipadx=200, padx=5, pady=5, fill='y')

        buttons_frame_1 = tk.LabelFrame(self.root)
        buttons_frame_1.pack(side='right', padx=5, pady=11, fill='both')


        button1 = tk.Button(buttons_frame, text="Editar", font='Helvetica 20 bold')
        button1.pack(fill='both', pady=10, padx=10)

        button2 = tk.Button(buttons_frame, text="Borrar", font='Helvetica 20 bold')
        button2.pack(fill='both', pady=10, padx=10)

        sub_buttons_frame = tk.Frame(buttons_frame)
        sub_buttons_frame.pack(side='bottom', fill='x')

        button3 = tk.Button(sub_buttons_frame, text="Regresar", font='Helvetica 15 bold')
        button3.pack(side='left', pady=10, padx=10)

        # Define Heading
        columns = ("Id", "Nombre", "Apellido", "Cédula", "Email", "Teléfono fijo", "Celular", "Direccion")
        treeview = ttk.Treeview(buttons_frame_1, height=18, show="headings", columns=columns)
        treeview.heading("Id", text="Id")
        treeview.heading("Nombre", text="Nombre")
        treeview.heading("Apellido", text="Apellido")
        treeview.heading("Cédula", text="Cédula")
        treeview.heading("Email", text="Email")
        treeview.heading("Teléfono fijo", text="Teléfono fijo")
        treeview.heading("Celular", text="Celular")
        treeview.heading("Direccion", text="Direccion")

        # Define Column
        treeview.column("Id", stretch=0, width=20, anchor='center')
        treeview.column("Nombre",width=150, anchor='center')
        treeview.column("Apellido", width=150, anchor='center')
        treeview.column("Cédula", width=150, anchor='center')
        treeview.column("Email", width=150, anchor='center')
        treeview.column("Teléfono fijo", width=150, anchor='center')
        treeview.column("Celular", width=150, anchor='center')
        treeview.column("Direccion", width=150, anchor='center')

        # Insert Data
        clients = self.get_all_client()
        id = [client.get("client_id") for client in clients]
        name = [client.get("name") for client in clients]
        last_name = [client.get("last_name") for client in clients]
        identity_card = [client.get("identity_card") for client in clients]
        email = [client.get("email") for client in clients]
        phone_1 = [client.get("phone_1") for client in clients]
        phone_2 = [client.get("phone_2") for client in clients]
        address = [client.get("address") for client in clients]

        for client in range(0, len(clients)):
            treeview.insert('', client, values=(
                id[client],
                name[client],
                last_name[client],
                identity_card[client],
                email[client],
                phone_1[client],
                phone_2[client],
                address[client]))

        # Scrollbar
        scrollbar_vertical = ttk.Scrollbar(buttons_frame_1)
        scrollbar_vertical.configure(command=treeview.yview)
        treeview.configure(yscrollcommand=scrollbar_vertical.set)

        scrollbar_horizontal = ttk.Scrollbar(buttons_frame_1, orient="horizontal")
        scrollbar_horizontal.configure(command=treeview.xview)
        treeview.configure(xscrollcommand=scrollbar_horizontal.set)

        # Position
        scrollbar_vertical.pack(side="right", fill="y")
        scrollbar_horizontal.pack(side="bottom", fill="x")
        treeview.pack(side="right", fill='both', expand=True)

        self.root.mainloop()


