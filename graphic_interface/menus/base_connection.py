from backend.core.client import Client
from backend.core.vehicle import Vehicle
from backend.core.repair import Repair
from backend.core.vehicle_type import VehicleType


class BaseDatabase:
    """Class Base Database."""

    def __init__(self, connection):
        """Base Database init."""
        self.connection = connection
        self.client = Client(connection=self.connection)
        self.vehicle = Vehicle(connection=self.connection)
        self.repair = Repair(connection=self.connection)
        self.vehicle_type = VehicleType(connection=self.connection)
