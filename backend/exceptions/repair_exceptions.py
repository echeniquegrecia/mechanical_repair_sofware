from backend.exceptions.base_exception import BaseException


class RepairDeleteException(BaseException):
    """Exception when there is an error in delete repair."""

    message = "Error to delete a repair."


class RepairUpdateException(BaseException):
    """Exception when there is an error in update repair."""

    message = "Error to update a repair."


class RepairCreateException(BaseException):
    """Exception when there is an error in creating repair."""

    message = "Error to create a repair."


class RepairGetCategoryException(BaseException):
    """Exception when there is an error to get a specific item."""

    message = "Error to get category of a repair."


class RepairGetAllException(BaseException):
    """Exception when there is an error to get all the repairs."""

    message = "Error to get all the repairs."


class RepairFormatDataException(BaseException):
    """Exception when there is an error in format data."""

    message = "Error in format data repair."
