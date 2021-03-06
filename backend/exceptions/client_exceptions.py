from backend.exceptions.base_exception import BaseException


class ClientDeleteException(BaseException):
    """Exception when there is an error in delete client."""

    message = "Error to delete a client."


class ClientUpdateException(BaseException):
    """Exception when there is an error in update client."""

    message = "Error to update a client."


class ClientCreateException(BaseException):
    """Exception when there is an error in creating client."""

    message = "Error to create a client."


class ClientGetCategoryException(BaseException):
    """Exception when there is an error to get a specific item."""

    message = "Error to get category of a client."


class ClientGetAllException(BaseException):
    """Exception when there is an error to get all the clients."""

    message = "Error to get all the clients."


class ClientFormatDataException(BaseException):
    """Exception when there is an error in format data."""

    message = "Error in format data client."
