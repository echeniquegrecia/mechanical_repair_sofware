import tkinter as tk
from PIL import Image, ImageTk

from graphic_interface.menus.base_frame import BaseFrame
from graphic_interface.menus.client.menu_client import MenuClient
from settings import IMAGE_MENU


class MenuHome(BaseFrame):
    """Class for MenuHome."""

    def __init__(self, root, connection):
        """MenuHome init."""
        super().__init__(root=root, connection=connection)
        self.root.state('zoomed')

        frame_1 = tk.LabelFrame(self.root, text="Menu", width=100, height=10)
        frame_1.pack(side='left', ipadx=100, padx=5, pady=5, fill='y')

        frame_2 = tk.LabelFrame(self.root, width=300)
        frame_2.pack(side='right', ipadx=320, padx=5, pady=11, fill='both')

        button_1 = tk.Button(frame_1, text="Clientes", font='Helvetica 20 bold', command=self.menu_client)
        button_1.pack(fill='both', pady=10, padx=10)

        button_2 = tk.Button(frame_1, text="Vehiculos", font='Helvetica 20 bold')
        button_2.pack(fill='both', pady=10, padx=10)

        button_3 = tk.Button(frame_1, text="Reparaciones", font='Helvetica 20 bold')
        button_3.pack(fill='both', pady=10, padx=10)

        frame_3 = tk.Frame(frame_1, height=100)
        frame_3.pack(fill='both', pady=10, padx=10, expand=True)

        frame_4 = tk.Frame(frame_3)
        frame_4.pack(side='bottom', fill='x')

        button_4 = tk.Button(frame_4, text="Salir", font='Helvetica 15 bold', width=15)
        button_4.pack(side='right', fil='x')

        button_5 = tk.Button(frame_4, text="Reset", font='Helvetica 15 bold', width=15)
        button_5.pack(side='left', fil='x')

        image = Image.open(IMAGE_MENU)
        image = image.resize((950, 800), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        label = tk.Label(frame_2, image=image)
        label.pack(side='right', fill='both', expand=True)

        self.root.mainloop()

    def menu_client(self):
        """Open menu client."""
        self.hide()
        self.new_window = tk.Toplevel(self.root)
        self.app = MenuClient(root=self.new_window, connection=self.connection, master=self)
