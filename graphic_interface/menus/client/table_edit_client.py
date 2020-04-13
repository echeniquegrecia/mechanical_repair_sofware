import tkinter as tk
from tkinter import ttk
from graphic_interface.menus.base_frame import BaseFrame
from graphic_interface.menus.client.form_edit_client import FormEditClient


class TableEditClient(BaseFrame):
    """Class for Table Edit Client Window."""

    def __init__(self, root, connection, master):
        """Edit Client Window init."""
        super().__init__(root=root, connection=connection)
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

        frame_1 = tk.LabelFrame(self.root, text="Editar-Borrar Client", width=100, height=10)
        frame_1.pack(side='left', ipadx=200, padx=5, pady=5, fill='y')

        frame_2 = tk.LabelFrame(self.root)
        frame_2.pack(side='right', padx=5, pady=11, fill='both')

        button_1 = tk.Button(frame_1, text="Editar", font='Helvetica 20 bold', command=self.form_edit_client)
        button_1.pack(fill='both', pady=10, padx=10)

        button_2 = tk.Button(frame_1, text="Actualizar", font='Helvetica 20 bold', command=self.update_table)
        button_2.pack(fill='both', pady=10, padx=10)

        frame_3 = tk.Frame(frame_1)
        frame_3.pack(side='bottom', fill='x')

        button_3 = tk.Button(frame_3, text="Regresar", font='Helvetica 15 bold', command=self.go_back)
        button_3.pack(side='left', pady=10, padx=10)

        # Define Heading table
        columns = ("Id", "Nombre", "Apellido", "Cédula", "Email", "Teléfono fijo", "Celular", "Direccion")
        self.treeview = ttk.Treeview(frame_2, height=18, show="headings", columns=columns)
        self.treeview.heading("Id", text="Id")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Apellido", text="Apellido")
        self.treeview.heading("Cédula", text="Cédula")
        self.treeview.heading("Email", text="Email")
        self.treeview.heading("Teléfono fijo", text="Teléfono fijo")
        self.treeview.heading("Celular", text="Celular")
        self.treeview.heading("Direccion", text="Direccion")

        # Define Columns table
        self.treeview.column("Id", stretch=0, width=20, anchor='center')
        self.treeview.column("Nombre",width=150, anchor='center')
        self.treeview.column("Apellido", width=150, anchor='center')
        self.treeview.column("Cédula", width=150, anchor='center')
        self.treeview.column("Email", width=150, anchor='center')
        self.treeview.column("Teléfono fijo", width=150, anchor='center')
        self.treeview.column("Celular", width=150, anchor='center')
        self.treeview.column("Direccion", width=150, anchor='center')

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
            self.treeview.insert('', client, values=(
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
        scrollbar_vertical.configure(command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=scrollbar_vertical.set)

        # Scrollbar Horizontal
        scrollbar_horizontal = ttk.Scrollbar(frame_2, orient="horizontal")
        scrollbar_horizontal.configure(command=self.treeview.xview)
        self.treeview.configure(xscrollcommand=scrollbar_horizontal.set)

        # Scrollbar Position
        scrollbar_vertical.pack(side="right", fill="y")
        scrollbar_horizontal.pack(side="bottom", fill="x")
        self.treeview.pack(side="right", fill='both', expand=True)

        self.root.mainloop()

    def form_edit_client(self):
        """Open Form Edit Client."""
        values = self.get_values()

        if not values:
            self.show_error(message="Por favor seleccione un cliente.")
        self.new_window = tk.Toplevel(self.root)
        self.app = FormEditClient(root=self.new_window, connection=self.connection, master=self, values=values)

    def get_values(self):
        """Get values."""
        cur_item = self.treeview.focus()
        item = self.treeview.item(cur_item)
        values = item.get("values", [])
        return values

    def go_back(self):
        """Go back to Menu Client."""
        self.hide()
        self.master.show()

    def update_table(self):
        """Update table."""
        clients = self.client.get_all()
        id = [client.get("client_id") for client in clients]
        name = [client.get("name") for client in clients]
        last_name = [client.get("last_name") for client in clients]
        identity_card = [client.get("identity_card") for client in clients]
        email = [client.get("email") for client in clients]
        phone_1 = [client.get("phone_1") for client in clients]
        phone_2 = [client.get("phone_2") for client in clients]
        address = [client.get("address") for client in clients]

        for i in self.treeview.get_children():
            self.treeview.delete(i)

        for client in range(0, len(clients)):
            self.treeview.insert('', client, values=(
                id[client],
                name[client],
                last_name[client],
                identity_card[client],
                email[client],
                phone_1[client],
                phone_2[client],
                address[client]))