import tkinter as tk
from tkinter import ttk

from backend.exceptions.client_exceptions import ClientDeleteException, ClientGetCategoryException
from graphic_interface.menus.base_frame import BaseFrame
from graphic_interface.menus.client.form_edit_client import FormEditClient
from graphic_interface.menus.client.form_new_client import FormNewClient


class MenuClient(BaseFrame):
    """Class for Menu Client Window."""

    def __init__(self, root, connection, master):
        """Menu Client init."""
        super().__init__(root=root, connection=connection)
        self.root.state('zoomed')
        self.root['bg'] = 'black'
        self.master = master
        self.data = {
            "brand": tk.StringVar(),
            "model": tk.StringVar(),
            "year": tk.StringVar()
        }

        frame_1 = tk.LabelFrame(self.root, text="Menu Cliente", width=100, height=10, bg="black", foreground="white", font='bold')
        frame_1.pack(side='top', padx=5, pady=5, fill='x')

        frame_2 = tk.LabelFrame(self.root, width=100, height=10, bg="black")
        frame_2.pack(side='left', ipadx=100, padx=5, pady=5, fill='y')

        frame_3 = tk.LabelFrame(self.root, bg="black")
        frame_3.pack(side='left', padx=5, pady=5, fill='both', expand=True)

        button_1 = tk.Button(frame_2, text="Nuevo", font='Helvetica 20 bold', width=15, bg="gold2", command=self.create_new_client)
        button_1.pack(fill='both', pady=10, padx=10)

        button_2 = tk.Button(frame_2, text="Editar", font='Helvetica 20 bold', width=15, bg="gold2", command=self.edit_client)
        button_2.pack(fill='both', pady=10, padx=10)

        button_3 = tk.Button(frame_2, text="Borrar", font='Helvetica 20 bold', width=15, bg="gold2", command=self.delete_client)
        button_3.pack(fill='both', pady=10, padx=10)

        button_4 = tk.Button(frame_2, text="Refrescar tabla", font='Helvetica 20 bold', bg="gold2", command=self.refresh_table)
        button_4.pack(fill='both', pady=10, padx=10)

        frame_4 = tk.Frame(frame_2, bg="black")
        frame_4.pack(side='bottom', fill='x')

        button_5 = tk.Button(frame_4, text="Regresar", font='Helvetica 15 bold', bg="gold2", command=self.go_back)
        button_5.pack(side='left', pady=10, padx=10)

        # Define search frame
        self.option_var = tk.StringVar()
        self.option_var.set("--Seleccione una busqueda--")
        contents = {"Nombre", "Apellido", "Cédula", "Email"}
        self.options = tk.OptionMenu(frame_1, self.option_var, *contents)
        self.options.config(font=('Helvetica', 15), bg="gold2")
        self.options.pack(side='left', pady=10, padx=10, fill='x')

        self.entry_var = tk.StringVar()
        entry = tk.Entry(frame_1, font="Helvetica 15", textvariable=self.entry_var)
        entry.pack(side='left', pady=10, padx=10, fill='x')

        button_6 = tk.Button(frame_1, text="Buscar", font='Helvetica 15 bold', bg="gold2", command=self.search_client_by_category)
        button_6.pack(side='left', pady=10, padx=10, fill='x')

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
        self.treeview.column("Nombre", width=150, anchor='center')
        self.treeview.column("Apellido", width=150, anchor='center')
        self.treeview.column("Cédula", width=150, anchor='center')
        self.treeview.column("Email", width=150, anchor='center')
        self.treeview.column("Teléfono fijo", width=150, anchor='center')
        self.treeview.column("Celular", width=150, anchor='center')
        self.treeview.column("Direccion", width=250, anchor='center')

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

    def create_new_client(self):
        """Create new client."""
        self.new_window = tk.Toplevel(self.root)
        self.app = FormNewClient(root=self.new_window, connection=self.connection, master=self)

    def edit_client(self):
        """Edit Client."""
        values = self.get_values()
        if not values:
            self.show_error(message="Por favor seleccione un cliente.")
        self.new_window = tk.Toplevel(self.root)
        self.app = FormEditClient(root=self.new_window, connection=self.connection, master=self, values=values)

    def delete_client(self):
        """Delete Client."""
        values = self.get_values()
        if not values:
            self.show_error(message="Por favor seleccione un cliente.")
        id = values[0]
        try:
            self.client.delete(client_id=id)
            self.refresh_table()
            self.show_info(message=f"El cliente ha sido borrado exitosamente.")
        except ClientDeleteException as error:
            if "vehicle registered" in error.message:
                self.show_error(message=f"El cliente tiene un vehiculo registrado. Por favor, borre el vehiculo y luego el cliente.")
            self.show_error(message=f"Error al borrar el cliente.")

    def get_client_by_category(self):
        """Get client by category."""
        try:
            category = {
                "Nombre": self.client.get_by_name(name=self.entry_var.get()),
                "Apellido": self.client.get_by_last_name(last_name=self.entry_var.get()),
                "Cédula": self.client.get_by_identity_card(identity_card=self.entry_var.get()),
                "Email": self.client.get_by_email(email=self.entry_var.get())

            }
        except ClientGetCategoryException:
            self.show_error(message=f"Error al buscar cliente.")
            raise ClientGetCategoryException()
        return category[self.option_var.get()]

    def search_client_by_category(self):
        """Search client by category."""
        clients = self.get_client_by_category()
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

    def go_back(self):
        """Go back to Menu Client."""
        self.hide()
        self.master.show()

    def refresh_table(self):
        """Refresh table."""
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
