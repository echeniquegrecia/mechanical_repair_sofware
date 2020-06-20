class CheckVehicleDataFormat:
    """Check the Vehicle Data Format."""

    def __init__(self, vehicle_type_data: dict):
        """Check Vehicle Type Data Format init.

        vehicle_type_id: Vehicle type ID
        identity": Identity of the vehicle
        color: Vehicle color.
        """

        for key, value in vehicle_type_data.items():
            vehicle_type_data[key] = None if value == "" else value
