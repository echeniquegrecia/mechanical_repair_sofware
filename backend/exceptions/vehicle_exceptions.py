from backend.exceptions.base_exception import BaseException


class VehicleDeleteException(BaseException):
    """Exception when there is an error in delete vehicle."""

    message = "Error to delete a vehicle."


class VehicleUpdateException(BaseException):
    """Exception when there is an error in update vehicle."""

    message = "Error to update a vehicle."


class VehicleCreateException(BaseException):
    """Exception when there is an error in creating vehicle."""

    message = "Error to create a vehicle."


class VehicleGetCategoryException(BaseException):
    """Exception when there is an error to get a specific item."""

    message = "Error to get category of a vehicle."


class VehicleGetAllException(BaseException):
    """Exception when there is an error to get all the vehicles."""

    message = "Error to get all the vehicles."


class VehicleFormatDataException(BaseException):
    """Exception when there is an error in format data."""

    message = "Error in format data vehicle."
