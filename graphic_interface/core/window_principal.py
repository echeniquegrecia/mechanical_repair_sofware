import tkinter as tk
from PIL import Image, ImageTk

from graphic_interface.core.client.menu_client import MenuClient
from settings import IMAGE_MENU


class WindowPrincipal:
    """Class for Window Principal."""

    def __init__(self):
        """Window Principal init"""
        self.root = tk.Tk()
        self.root.title('Taller Mecanico Echenique - Programa de gestion')
        self.root.state('zoomed')

        buttons_frame = tk.LabelFrame(self.root, text="Menu", width=100, height=10)
        buttons_frame.pack(side='left', ipadx=100, padx=5, pady=5, fill='y')

        buttons_frame_1 = tk.LabelFrame(self.root, width=300)
        buttons_frame_1.pack(side='right', ipadx=320, padx=5, pady=11, fill='both')

        image = Image.open(IMAGE_MENU)
        image = image.resize((950, 800), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        label = tk.Label(buttons_frame_1, image=image)
        label.pack(side='right', fill='both', expand=True)

        button1 = tk.Button(buttons_frame, text="Clientes", font='Helvetica 20 bold', command=MenuClient)
        button1.pack(fill='both', pady=10, padx=10)

        button2 = tk.Button(buttons_frame, text="Vehiculos", font='Helvetica 20 bold')
        button2.pack(fill='both', pady=10, padx=10)

        button3 = tk.Button(buttons_frame, text="Reparaciones", font='Helvetica 20 bold')
        button3.pack(fill='both', pady=10, padx=10)

        sub_buttons_frame = tk.Frame(buttons_frame, height=100)
        sub_buttons_frame.pack(fill='both', pady=10, padx=10, expand=True)

        sub_buttons_frame_2 = tk.Frame(sub_buttons_frame)
        sub_buttons_frame_2.pack(side='bottom', fill='x')

        buttonW = tk.Button(sub_buttons_frame_2, text="Salir", font='Helvetica 15 bold', width=15)
        buttonW.pack(side='right', fil='x')

        buttonE = tk.Button(sub_buttons_frame_2, text="Configuracion", font='Helvetica 15 bold', width=15)
        buttonE.pack(side='left', fil='x')

        self.root.mainloop()


