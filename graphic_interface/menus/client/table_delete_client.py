import tkinter as tk
from tkinter import ttk
from graphic_interface.menus.base_frame import BaseFrame


class TableDeleteClient(BaseFrame):
    """Class for Table Delete Client Window."""

    def __init__(self, root, connection, master):
        """Search Client Window init."""
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

        frame_1 = tk.LabelFrame(self.root, text="Borrar Client", width=100, height=10)
        frame_1.pack(side='top', padx=5, pady=5, fill='both', expand=True)

        frame_2 = tk.LabelFrame(frame_1)
        frame_2.pack(side='top', padx=5, pady=11, fill='both')

        frame_3 = tk.LabelFrame(frame_1)
        frame_3.pack(side='top', padx=5, pady=11, fill='both', expand=True)

        self.option_var = tk.StringVar()
        self.option_var.set("--Seleccione una busqueda--")
        contents = {"Nombre", "Apellido", "Cédula", "Email"}
        self.options = tk.OptionMenu(frame_2, self.option_var, *contents)
        self.options.config(font=('Helvetica', 15))
        self.options.pack(side='left', pady=10, padx=10, fill='x')

        self.entry_var = tk.StringVar()
        entry = tk.Entry(frame_2, font="Helvetica 15", textvariable=self.entry_var)
        entry.pack(side='left', pady=10, padx=10, fill='x')

        button_3 = tk.Button(frame_2, text="Buscar", font='Helvetica 15 bold', command=self.search_client_by_category)
        button_3.pack(side='left', pady=10, padx=10, fill='x')

        button_4 = tk.Button(frame_2, text="Borrar", font='Helvetica 15 bold', command=self.delete_client)
        button_4.pack(side='left', pady=10, padx=10, fill='x')

        button_5 = tk.Button(frame_2, text="Refrescar", font='Helvetica 15 bold', command=self.clean_table)
        button_5.pack(side='left', pady=10, padx=10, fill='x')

        frame_4 = tk.Frame(frame_1)
        frame_4.pack(side='bottom', fill='x')

        button_6 = tk.Button(frame_4, text="Regresar", font='Helvetica 15 bold', command=self.go_back)
        button_6.pack(side='right', pady=10, padx=10)

        # Define Heading table
        columns = ("Id", "Nombre", "Apellido", "Cédula", "Email", "Teléfono fijo", "Celular", "Direccion")
        self.treeview = ttk.Treeview(frame_3, height=18, show="headings", columns=columns)
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
        scrollbar_vertical = ttk.Scrollbar(frame_3)
        scrollbar_vertical.configure(command=self.treeview.yview)
        self.treeview.configure(yscrollcommand=scrollbar_vertical.set)

        # Scrollbar Horizontal
        scrollbar_horizontal = ttk.Scrollbar(frame_3, orient="horizontal")
        scrollbar_horizontal.configure(command=self.treeview.xview)
        self.treeview.configure(xscrollcommand=scrollbar_horizontal.set)

        # Scrollbar Position
        scrollbar_vertical.pack(side="right", fill="y")
        scrollbar_horizontal.pack(side="bottom", fill="x")
        self.treeview.pack(side="right", fill='both', expand=True)

        self.root.mainloop()

    def get_client_by_item(self):
        """Get client."""
        item = {
            "Nombre": self.client.get_by_name(name=self.entry_var.get()),
            "Apellido": self.client.get_by_last_name(last_name=self.entry_var.get()),
            "Cédula": self.client.get_by_identity_card(identity_card=self.entry_var.get()),
            "Email": self.client.get_by_email(email=self.entry_var.get())
        }
        return item[self.option_var.get()]

    def search_client_by_category(self):
        """Search client by category."""
        clients = self.get_client_by_item()
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

    def clean_table(self):
        """Clean table."""
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

    def get_values(self):
        """Get values."""
        cur_item = self.treeview.focus()
        item = self.treeview.item(cur_item)
        values = item.get("values", [])
        return values

    def delete_client(self):
        """Delete client."""
        client = self.get_values()
        if not client:
            self.show_error(message="Por favor seleccione un cliente.")
        try:
            client_id = client[0]
            client_name = client[1]
            client_last_name = client[2]
            self.client.delete(client_id=client_id)
            self.show_info(message=f"El cliente: {client_name} {client_last_name} fue borrado exitosamente.")
        except Exception as error:
            self.show_error(message=f"El cliente no pudo ser eliminado. {error}")

    def go_back(self):
        """Go back to Menu Client."""
        self.hide()
        self.master.show()
