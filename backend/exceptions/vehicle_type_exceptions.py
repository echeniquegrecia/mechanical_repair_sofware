from backend.exceptions.base_exception import BaseException


class VehicleTypeCreateException(BaseException):
    """Exception when there is an error in creating vehicle type."""

    message = "Error to create a vehicle type."


class VehicleTypeUpdateException(BaseException):
    """Exception when there is an error in update vehicle type."""

    message = "Error to update a vehicle type."


class VehicleTypeDeleteException(BaseException):
    """Exception when there is an error in delete vehicle type."""

    message = "Error to delete a vehicle type."


class VehicleTypeFormatDataException(BaseException):
    """Exception when there is an error in format data."""

    message = "Error in format data vehicle type."


class VehicleTypeGetCategoryException(BaseException):
    """Exception when there is an error to get a specific item."""

    message = "Error to get vehicle type of a client."


class VehicleTypeGetAllException(BaseException):
    """Exception when there is an error to get all the vehicle types."""

    message = "Error to get all the vehicle types."
