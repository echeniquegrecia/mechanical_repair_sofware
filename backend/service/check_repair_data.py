import time
from backend.exceptions.repair_exceptions import RepairFormatDataException


class CheckRepairDataFormat:
    """Check the Repair Data Format."""

    def __init__(self, repair_data: dict):
        """Check Repair Type Data Format init.

        vehicle_id: vehicle id
        mileage: mileage vehicle
        client_observations: observation from clients
        mechanical_observations: observations from mechanical
        final_observations: observations post reparation
        date_entry:
        date_exit:
        price:
        status: "EN TALLER", "FINALIZADO".
        """
        # Check dates
        self.dates(
            date_entry=repair_data["date_entry"],
            date_exit=repair_data["date_exit"]
        )
        # Check status
        self. status(status=repair_data["status"])
        # Check mileage
        self.mileage(mileage=repair_data["mileage"])
        # Check price
        self.price(price=repair_data["price"])
        # Check status and date exit
        self.status_and_date_exit(
            status=repair_data["status"],
            date_exit=repair_data["date_exit"]
        )


    @staticmethod
    def dates(date_entry: str, date_exit: str):
        """Check entry and exit dates."""
        if date_entry and date_exit:
            date_entry = time.strptime(date_entry, "%d/%m/%Y")
            date_exit = time.strptime(date_exit, "%d/%m/%Y")
            if date_entry > date_exit:
                message = "Date entry can not be newer than Date exit."
                raise RepairFormatDataException(message=message)

    @staticmethod
    def status(status: str):
        """Check status values."""
        if status not in ["EN TALLER", "FINALIZADO"]:
            message = "The status value is not in [EN TALLER, FINALIZADO]"
            raise RepairFormatDataException(message=message)

    @staticmethod
    def mileage(mileage: str):
        """Check mileage."""
        if mileage:
            try:
                float(mileage)
            except:
                message = "The mileage value is not correct"
                raise RepairFormatDataException(message=message)

    @staticmethod
    def price(price: str):
        """Check price."""
        if price:
            try:
                float(price)
            except:
                message = "The price value is not correct"
                raise RepairFormatDataException(message=message)

    @staticmethod
    def status_and_date_exit(status: str, date_exit: str):
        """Check status and date exit."""
        if status != "FINALIZADO" and date_exit:
            message = "Status must be closed"
            raise RepairFormatDataException(message=message)

        if status == "FINALIZADO" and not date_exit:
            message = "Date exit is missing"
            raise RepairFormatDataException(message=message)
