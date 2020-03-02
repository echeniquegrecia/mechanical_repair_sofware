import tkinter as tk

class FormNewClient:
    """Class FormNewClient."""

    def __init__(self, root):
        """FormNewClient init."""
        self.root = root
        self.root.title('Taller Mecanico Echenique - Programa de gestion')
        self.root.state('zoomed')

        buttons_frame = tk.LabelFrame(self.root, text="Nuevo cliente")
        buttons_frame.pack(side="left",padx=5, pady=5, fill='both', expand=True)

        buttons_frame_2 = tk.Frame(buttons_frame)
        buttons_frame_2.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        buttons_frame_3 = tk.Frame(buttons_frame)
        buttons_frame_3.pack(side="left", fill='x', padx=5, pady=5, expand=True)

        # buttons_frame_4 = tk.Frame(buttons_frame)
        # buttons_frame_4.pack(fill='x', padx=5, pady=5, expand=True)
        #
        # buttons_frame_5 = tk.Frame(buttons_frame)
        # buttons_frame_5.pack(fill='x', padx=5, pady=5, expand=True)

        name_label = tk.Label(buttons_frame_2, text="Nombre", font='Helvetica 18 bold')
        name_label.pack(padx=5, pady=5, expand=True)
        name_entry = tk.Entry(buttons_frame_3, font = "Helvetica 15", width=100)
        name_entry.pack(padx=5, pady=5, fill='both')

        # last_name_label = tk.Label(buttons_frame_2, text="Apellido", font='Helvetica 18 bold')
        # last_name_label.pack(side="left", padx=5, pady=5, fill='both')
        # last_name_entry = tk.Entry(buttons_frame_2, font = "Helvetica 15", width=100)
        # last_name_entry.pack(side="left", padx=5, pady=5, fill='both')

        identity_card_label = tk.Label(buttons_frame_2, text="Cedula", font='Helvetica 18 bold')
        identity_card_label.pack(padx=5, pady=5, expand=True)
        identity_card_entry = tk.Entry(buttons_frame_3, font="Helvetica 15", width=100)
        identity_card_entry.pack(padx=5, pady=5, fill='both')

        # email_label = tk.Label(buttons_frame_3, text="Email", font='Helvetica 18 bold')
        # email_label.pack(side="left", padx=5, pady=5, fill='both')
        # email_entry = tk.Entry(buttons_frame_3, font="Helvetica 15", width=100)
        # email_entry.pack(side="left", padx=5, pady=5, fill='both')
        #
        phone_1_label = tk.Label(buttons_frame_2, text="Telefono fijo", font='Helvetica 18 bold')
        phone_1_label.pack(padx=5, pady=5, expand=True)
        phone_1_entry = tk.Entry(buttons_frame_3, font="Helvetica 15", width=100)
        phone_1_entry.pack(padx=5, pady=5, fill='both')
        #
        # phone_2_label = tk.Label(buttons_frame_4, text="Celular", font='Helvetica 18 bold')
        # phone_2_label.pack(side="left", padx=5, pady=5, fill='both')
        # phone_2_entry = tk.Entry(buttons_frame_4, font="Helvetica 15", width=100)
        # phone_2_entry.pack(side="left", padx=5, pady=5, fill='both')
        #
        # address_label = tk.Label(buttons_frame_5, text="Direccion", font='Helvetica 18 bold')
        # address_label.pack(side="left", padx=5, pady=5, fill='both')
        # address_entry = tk.Entry(buttons_frame_5, font="Helvetica 15")
        # address_entry.pack(side="left", padx=5, pady=5, fill='both', expand=True)



















        # buttons_frame_2 = tk.Frame(buttons_frame)
        # buttons_frame_2.pack(fill='x', padx=5, pady=5)
        #
        # buttons_frame_3 = tk.Frame(buttons_frame)
        # buttons_frame_3.pack(fill='x', padx=5, pady=5)
        #
        # buttons_frame_4 = tk.Frame(buttons_frame)
        # buttons_frame_4.pack(fill='x', padx=5, pady=5)
        #
        # buttons_frame_5 = tk.Frame(buttons_frame)
        # buttons_frame_5.pack(fill='x', padx=5, pady=5)
        #
        # name_label = tk.Label(buttons_frame_2, text="Nombre", font='Helvetica 18 bold')
        # name_label.pack(side="left", padx=5, pady=5, fill='both')
        # name_entry = tk.Entry(buttons_frame_2, font = "Helvetica 15", width=100)
        # name_entry.pack(side="left", padx=5, pady=5, fill='both')
        #
        # last_name_label = tk.Label(buttons_frame_2, text="Apellido", font='Helvetica 18 bold')
        # last_name_label.pack(side="left", padx=5, pady=5, fill='both')
        # last_name_entry = tk.Entry(buttons_frame_2, font = "Helvetica 15", width=100)
        # last_name_entry.pack(side="left", padx=5, pady=5, fill='both')
        #
        # identity_card_label = tk.Label(buttons_frame_3, text="Cedula", font='Helvetica 18 bold')
        # identity_card_label.pack(side="left", padx=5, pady=5, fill='both')
        # identity_card_entry = tk.Entry(buttons_frame_3, font="Helvetica 15", width=100)
        # identity_card_entry.pack(side="left", padx=5, pady=5, fill='both')
        #
        # email_label = tk.Label(buttons_frame_3, text="Email", font='Helvetica 18 bold')
        # email_label.pack(side="left", padx=5, pady=5, fill='both')
        # email_entry = tk.Entry(buttons_frame_3, font="Helvetica 15", width=100)
        # email_entry.pack(side="left", padx=5, pady=5, fill='both')
        #
        # phone_1_label = tk.Label(buttons_frame_4, text="Telefono fijo", font='Helvetica 18 bold')
        # phone_1_label.pack(side="left", padx=5, pady=5, fill='both')
        # phone_1_entry = tk.Entry(buttons_frame_4, font="Helvetica 15", width=100)
        # phone_1_entry.pack(side="left", padx=5, pady=5, fill='both')
        #
        # phone_2_label = tk.Label(buttons_frame_4, text="Celular", font='Helvetica 18 bold')
        # phone_2_label.pack(side="left", padx=5, pady=5, fill='both')
        # phone_2_entry = tk.Entry(buttons_frame_4, font="Helvetica 15", width=100)
        # phone_2_entry.pack(side="left", padx=5, pady=5, fill='both')
        #
        # address_label = tk.Label(buttons_frame_5, text="Direccion", font='Helvetica 18 bold')
        # address_label.pack(side="left", padx=5, pady=5, fill='both')
        # address_entry = tk.Entry(buttons_frame_5, font="Helvetica 15")
        # address_entry.pack(side="left", padx=5, pady=5, fill='both', expand=True)


        self.root.mainloop()