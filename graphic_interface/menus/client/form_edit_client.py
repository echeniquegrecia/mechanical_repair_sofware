import tkinter as tk
from tkinter import ttk


from graphic_interface.menus.base_frame import BaseFrame


class FormEditClient(BaseFrame):
    """Class for Edit Client Window."""

    def __init__(self, root, connection, master):
        """Edit Client Window init."""
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

        frame_1 = tk.LabelFrame(self.root, text="Editar-Borrar Client", width=100, height=10)
        frame_1.pack(side='left', ipadx=200, padx=5, pady=5, fill='y')

        frame_2 = tk.LabelFrame(self.root)
        frame_2.pack(side='right', padx=5, pady=11, fill='both')

        button_1 = tk.Button(frame_1, text="Editar", font='Helvetica 20 bold')
        button_1.pack(fill='both', pady=10, padx=10)

        button_2 = tk.Button(frame_1, text="Borrar", font='Helvetica 20 bold')
        button_2.pack(fill='both', pady=10, padx=10)

        frame_3 = tk.Frame(frame_1)
        frame_3.pack(side='bottom', fill='x')

        button_3 = tk.Button(frame_3, text="Regresar", font='Helvetica 15 bold')
        button_3.pack(side='left', pady=10, padx=10)

        # Define Heading table
        columns = ("Id", "Nombre", "Apellido", "Cédula", "Email", "Teléfono fijo", "Celular", "Direccion")
        treeview = ttk.Treeview(frame_2, height=18, show="headings", columns=columns)
        treeview.heading("Id", text="Id")
        treeview.heading("Nombre", text="Nombre")
        treeview.heading("Apellido", text="Apellido")
        treeview.heading("Cédula", text="Cédula")
        treeview.heading("Email", text="Email")
        treeview.heading("Teléfono fijo", text="Teléfono fijo")
        treeview.heading("Celular", text="Celular")
        treeview.heading("Direccion", text="Direccion")

        # Define Columns table
        treeview.column("Id", stretch=0, width=20, anchor='center')
        treeview.column("Nombre",width=150, anchor='center')
        treeview.column("Apellido", width=150, anchor='center')
        treeview.column("Cédula", width=150, anchor='center')
        treeview.column("Email", width=150, anchor='center')
        treeview.column("Teléfono fijo", width=150, anchor='center')
        treeview.column("Celular", width=150, anchor='center')
        treeview.column("Direccion", width=150, anchor='center')

        # Insert Data
        clients = self.client.get_all()
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

        # Scrollbar Vertical
        scrollbar_vertical = ttk.Scrollbar(frame_2)
        scrollbar_vertical.configure(command=treeview.yview)
        treeview.configure(yscrollcommand=scrollbar_vertical.set)

        # Scrollbar Horizontal
        scrollbar_horizontal = ttk.Scrollbar(frame_2, orient="horizontal")
        scrollbar_horizontal.configure(command=treeview.xview)
        treeview.configure(xscrollcommand=scrollbar_horizontal.set)

        # Scrollbar Position
        scrollbar_vertical.pack(side="right", fill="y")
        scrollbar_horizontal.pack(side="bottom", fill="x")
        treeview.pack(side="right", fill='both', expand=True)

        self.root.mainloop()
