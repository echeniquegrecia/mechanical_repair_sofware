import tkinter as tk
import tkinter.messagebox
from core.client import Client

class BaseFrame:
    """Class BaseFrame"""

    def __init__(self, root, connection):
        """BaseFrame init."""
        self.root = root
        self.connection = connection

    def hide(self):
        self.root.withdraw()

    def show(self):
        self.root.update()
        self.root.deiconify()

    def create_client(self, data):
        """Create Client"""
        client = Client(connection=self.connection)
        result = client.create(data=data)
        print(client.get_all())
        if result:
            tk.messagebox.showinfo('Popup Window(Title)', 'Success')
            self.root.mainloop()
        else:
            tk.messagebox.showinfo('Popup Window(Title)', 'Sorry, Client was not created')
            self.root.mainloop()


    def get_all_client(self):
        client = Client(connection=self.connection)
        client.get_all()

    def update_client(self, client_id, data):
        client = Client(connection=self.connection)
        client.update(client_id=client_id, data=data)

    def delete_client(self, client_id):
        client = Client(connection=self.connection)
        client.delete(client_id=client_id)
