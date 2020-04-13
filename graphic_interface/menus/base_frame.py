import tkinter as tk
import tkinter.messagebox
from backend.core.client import Client
from graphic_interface.menus.base_connection import BaseDatabase


class BaseFrame(BaseDatabase):
    """Class BaseFrame"""

    def __init__(self, root, connection):
        """BaseFrame init."""
        super().__init__(connection=connection)
        self.root = root
        self.root.title('Taller Mecanico Echenique - Programa de gestion')
        self.root.state('zoomed')

    def hide(self):
        """Hide a window."""
        self.root.withdraw()

    def show(self):
        """Show a window."""
        self.root.update()
        self.root.deiconify()

    def show_info(self, message):
        """Show info."""
        tk.messagebox.showinfo("Popup Window(Title)", message)
        self.root.mainloop()
