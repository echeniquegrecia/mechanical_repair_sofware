import tkinter as tk
from PIL import Image, ImageTk

from graphic_interface.menus.base_frame import BaseFrame
from graphic_interface.menus.client.form_new_client import FormNewClient

from settings import IMAGE_MENU_CLIENT


class MenuClient(BaseFrame):
    """Class for Window Principal."""

    def __init__(self, root, connection, master):
        """Window Principal init"""
        super().__init__(root=root, connection=connection)
        self.master = master
        self.root.title('Taller Mecanico Echenique - Programa de gestion')
        self.root.state('zoomed')

        buttons_frame = tk.LabelFrame(self.root, text="Menu", width=100, height=10)
        buttons_frame.pack(side='left', ipadx=200, padx=5, pady=5, fill='y')

        buttons_frame_1 = tk.LabelFrame(self.root, width=300)
        buttons_frame_1.pack(side='right', ipadx=320, padx=5, pady=11, fill='both')

        image = Image.open(IMAGE_MENU_CLIENT)
        image = image.resize((950, 800), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        label = tk.Label(buttons_frame_1, image=image)
        label.pack(side='right', fill='both', expand=True)

        button1 = tk.Button(buttons_frame, text="Nuevo", font='Helvetica 20 bold', command=self.form_new_client)
        button1.pack(fill='both', pady=10, padx=10)

        button2 = tk.Button(buttons_frame, text="Editar", font='Helvetica 20 bold')
        button2.pack(fill='both', pady=10, padx=10)

        button3 = tk.Button(buttons_frame, text="Buscar", font='Helvetica 20 bold')
        button3.pack(fill='both', pady=10, padx=10)

        button4 = tk.Button(buttons_frame, text="Borrar", font='Helvetica 20 bold')
        button4.pack(fill='both', pady=10, padx=10)

        sub_buttons_frame = tk.Frame(buttons_frame, height=100)
        sub_buttons_frame.pack(fill='both', pady=10, padx=10, expand=True)

        sub_buttons_frame_2 = tk.Frame(sub_buttons_frame)
        sub_buttons_frame_2.pack(side='bottom', fill='x')


        buttonE = tk.Button(sub_buttons_frame_2, text="Regresar", font='Helvetica 15 bold', command=self.go_back)
        buttonE.pack(side='left', fil='x')

        self.root.mainloop()

    def form_new_client(self):
        self.hide()
        self.newWindow = tk.Toplevel(self.root)
        self.app = FormNewClient(root=self.newWindow, connection=self.connection, master=self)

    def go_back(self):
        self.hide()
        self.master.show()