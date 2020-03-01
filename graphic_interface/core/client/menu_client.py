import tkinter as tk
from PIL import Image, ImageTk

from settings import IMAGE_MENU_CLIENT


class MenuClient:
    """Class for Window Principal."""

    def __init__(self):
        """Window Principal init"""
        self.root = tk.Toplevel()
        self.root.title('Taller Mecanico Echenique - Programa de gestion')
        self.root.state('zoomed')

        buttons_frame = tk.LabelFrame(self.root, text="Clientes", width=100, height=10)
        buttons_frame.pack(side='left', ipadx=250, padx=5, pady=5, fill='y')

        buttons_frame_1 = tk.LabelFrame(self.root, width=300)
        buttons_frame_1.pack(side='right', ipadx=320, padx=5, pady=11, fill='both')

        image = Image.open(IMAGE_MENU_CLIENT)
        print(IMAGE_MENU_CLIENT)
        image = image.resize((950, 800), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        label = tk.Label(buttons_frame_1, image=image)
        label.pack(side='right', fill='both', expand=True)

        button1 = tk.Button(buttons_frame, text="Nuevo", font='Helvetica 20 bold')
        button1.pack(fill='both', pady=10, padx=10)

        button2 = tk.Button(buttons_frame, text="Editar", font='Helvetica 20 bold')
        button2.pack(fill='both', pady=10, padx=10)

        button3 = tk.Button(buttons_frame, text="Buscar", font='Helvetica 20 bold')
        button3.pack(fill='both', pady=10, padx=10)

        self.root.mainloop()
