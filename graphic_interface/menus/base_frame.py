import tkinter as tk
import tkinter.messagebox
from graphic_interface.menus.base_connection import BaseDatabase


class BaseFrame(BaseDatabase):
    """Class BaseFrame"""

    def __init__(self, root, connection):
        """BaseFrame init."""
        super().__init__(connection=connection)
        self.root = root
        self.root.title('Taller Mecanico Echenique - Programa de gestion')

    def hide(self):
        """Hide a window."""
        self.root.withdraw()

    def show(self):
        """Show a window."""
        self.root.update()
        self.root.deiconify()

    def show_info(self, message):
        """Show info."""
        tk.messagebox.showinfo("Informacion", message)
        self.root.mainloop()

    def show_error(self, message):
        """Show error."""
        tk.messagebox.showerror("Error", message)
        self.root.mainloop()

    def ask_question(self, message_1, message_2, response_positive=None, response_negative=None):
        """Ask question dialog."""
        result = tk.messagebox.askquestion(message_1, message_2, icon='warning')
        return True if result == "yes" else False
