from backend.exceptions.vehicle_exceptions import VehicleMissingMandatoryDataException


class CheckVehicleDataFormat:
    """Check the Vehicle Data Format."""

    def __init__(self, vehicle_data: dict):
        """Check Vehicle Data Format init.

        vehicle_type_id: Vehicle type ID
        identity": Identity of the vehicle
        color: Vehicle color.
        """

        self.vehicle_data = vehicle_data
        self.missing_mandatory_data()

    def missing_mandatory_data(self):
        """Missing Mandatory Data."""
        for key, value in self.vehicle_data.items():
            if not value:
                raise VehicleMissingMandatoryDataException()
