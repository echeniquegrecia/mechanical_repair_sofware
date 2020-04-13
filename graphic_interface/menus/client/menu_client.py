import tkinter as tk
from PIL import Image, ImageTk

from graphic_interface.menus.base_frame import BaseFrame
from graphic_interface.menus.client.form_edit_client import FormEditClient
from graphic_interface.menus.client.form_new_client import FormNewClient

from settings import IMAGE_MENU_CLIENT


class MenuClient(BaseFrame):
    """Class for Menu Client Window."""

    def __init__(self, root, connection, master):
        """Menu Client init."""
        super().__init__(root=root, connection=connection)
        self.master = master

        frame_1 = tk.LabelFrame(self.root, text="Menu", width=100, height=10)
        frame_1.pack(side='left', ipadx=200, padx=5, pady=5, fill='y')

        frame_2 = tk.LabelFrame(self.root, width=300)
        frame_2.pack(side='right', ipadx=320, padx=5, pady=11, fill='both')

        button_1 = tk.Button(frame_1, text="Nuevo", font='Helvetica 20 bold', command=self.form_new_client)
        button_1.pack(fill='both', pady=10, padx=10)

        button_2 = tk.Button(frame_1, text="Editar", font='Helvetica 20 bold', command=self.form_edit_client)
        button_2.pack(fill='both', pady=10, padx=10)

        button_3 = tk.Button(frame_1, text="Buscar", font='Helvetica 20 bold')
        button_3.pack(fill='both', pady=10, padx=10)

        button_4 = tk.Button(frame_1, text="Borrar", font='Helvetica 20 bold')
        button_4.pack(fill='both', pady=10, padx=10)

        frame_3 = tk.Frame(frame_1, height=100)
        frame_3.pack(fill='both', pady=10, padx=10, expand=True)

        frame_4 = tk.Frame(frame_3)
        frame_4.pack(side='bottom', fill='x')

        button_5 = tk.Button(frame_4, text="Regresar", font='Helvetica 15 bold', command=self.go_back)
        button_5.pack(side='left', fil='x')

        image = Image.open(IMAGE_MENU_CLIENT)
        image = image.resize((950, 800), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        label = tk.Label(frame_2, image=image)
        label.pack(side='right', fill='both', expand=True)

        self.root.mainloop()

    def form_new_client(self):
        """Open window New Client."""
        self.hide()
        self.new_window = tk.Toplevel(self.root)
        self.app = FormNewClient(root=self.new_window, connection=self.connection, master=self)

    def form_edit_client(self):
        """Open window Edit Client."""
        self.hide()
        self.new_window = tk.Toplevel(self.root)
        self.app = FormEditClient(root=self.new_window, connection=self.connection, master=self)

    def go_back(self):
        """Go back Menu Home."""
        self.hide()
        self.master.show()
