import tkinter as tk

from backend.exceptions.vehicle_type_exceptions import VehicleTypeCreateException, VehicleTypeAlreadyExistsException, \
    VehicleTypeMissingMandatoryDataException
from backend.exceptions.vehicle_type_exceptions import VehicleTypeFormatDataException
from graphic_interface.menus.base_frame import BaseFrame


class FormNewVehicleType(BaseFrame):
    """Class for New Vehicle Type Window."""

    def __init__(self, root, connection, master):
        """New Client Window init."""
        super().__init__(root=root, connection=connection)
        self.master = master
        self.root['bg'] = 'black'
        self.data = {
            "brand": tk.StringVar(),
            "model": tk.StringVar(),
            "year": tk.StringVar()
        }

        frame_1 = tk.LabelFrame(self.root, text="Nuevo Tipo de Vehiculo", bg="black", foreground="white", font='bold')
        frame_1.pack(side="left",padx=5, pady=5, fill='both', expand=True)

        frame_2 = tk.Frame(frame_1, bg='black')
        frame_2.pack(side="top", padx=5, pady=5, fill='x')

        frame_3 = tk.Frame(frame_1, bg='black')
        frame_3.pack(side="bottom", padx=5, pady=5, fill='x')

        brand_label = tk.Label(frame_2, text="Marca", font='Helvetica 18 bold', anchor='w', foreground="gold2", bg= "black")
        brand_label.pack(padx=5, pady=5, fill='both')
        brand_entry = tk.Entry(frame_2, font = "Helvetica 17", textvariable=self.data["brand"])
        brand_entry.pack(padx=5, pady=5, fill='both')

        model_label = tk.Label(frame_2, text="Modelo", font='Helvetica 18 bold', anchor='w', foreground="gold2", bg= "black")
        model_label.pack(padx=5, pady=5, fill='both')
        model_entry = tk.Entry(frame_2, font = "Helvetica 17", textvariable=self.data["model"])
        model_entry.pack(padx=5, pady=5, fill='both')

        year_label = tk.Label(frame_2, text="Año", font='Helvetica 18 bold', anchor='w', foreground="gold2", bg= "black")
        year_label.pack(padx=5, pady=5, fill='both')
        year_entry = tk.Entry(frame_2, font="Helvetica 17", textvariable=self.data["year"])
        year_entry.pack(padx=5, pady=5, fill='both')

        button_1 = tk.Button(frame_3, text="Crear", font='Helvetica 15 bold', width=15, bg="gold2", command=self.create_new_vehicle_type)
        button_1.pack(side='right', fil='x')

        button_2 = tk.Button(frame_3, text="Regresar", font='Helvetica 15 bold', width=15, bg="gold2", command=self.go_back)
        button_2.pack(side='right', fil='x')

        self.root.mainloop()

    def create_new_vehicle_type(self):
        """Create new vehicle type."""
        brand = self.data["brand"].get()
        model = self.data["model"].get()
        year = self.data["year"].get()

        try:
            self.vehicle_type.create(
                brand=brand,
                model=model,
                year=year
            )
            self.show_info(message="El tipo de vehiculo ha sido registrado exitosamente")
        except VehicleTypeCreateException:
            self.show_error(message="ERROR: El tipo de vehiculo no ha sido creado. Por favor verifique que todos los datos estan completos")
        except VehicleTypeFormatDataException as error:
            if "brand" in error.message:
                self.show_error(message="ERROR: El formato de la marca es incorrecta.")
            if "model" in error.message:
                self.show_error(message="ERROR: El formato del modelo es incorrecta.")
            if "year" in error.message:
                self.show_error(message="ERROR: El formato del año es incorrecta.")
        except VehicleTypeAlreadyExistsException:
            self.show_error(message="ERROR: El tipo de vehiculo ya existe.")
        except VehicleTypeMissingMandatoryDataException:
            self.show_error(message=
                            "ERROR: Falta algunos datos obligatorios."
                            "Por favor verifique el ingreso del Modelo, Marca y Ano.")

    def go_back(self):
        """Go back to Menu Client."""
        self.hide()
        self.master.show()
