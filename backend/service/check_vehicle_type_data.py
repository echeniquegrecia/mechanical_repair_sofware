from backend.exceptions.vehicle_type_exceptions import VehicleTypeFormatDataException, \
    VehicleTypeMissingMandatoryDataException


class CheckVehicleTypeDataFormat:
    """Check the Vehicle Type Data Format."""

    def __init__(self, vehicle_type_data: dict):
        """Check Vehicle Type Data Format init.

        brand: str vehicle brand
        model: str vehicle model
        year: str vehicle year.
        """
        self.vehicle_type_data = vehicle_type_data
        self.missing_data_mandatory()
        for key, value in self.vehicle_type_data.items():
            try:
                if key == "brand":
                    isinstance(value, str)
                if key == "model":
                    isinstance(value, str)
                if key == "year":
                    isinstance(int(value), int)
            except Exception:
                message = f"Invalid Format in {key}"
                raise VehicleTypeFormatDataException(message=message)

    def missing_data_mandatory(self):
        """Check missing data mandatory."""
        for key, value in self.vehicle_type_data.items():
            if not value:
                raise VehicleTypeMissingMandatoryDataException()