from backend.exceptions.base_exception import BaseException


class ClientDeleteException(BaseException):
    """Exception when there is an error in delete client."""

    message = "Error to delete a client."


class ClientUpdateException(BaseException):
    """Exception when there is an error in update client."""

    message = "Error to update a client."


from backend.exceptions.base_exception import BaseException

class ClientCreateException(BaseException):
    """Exception when there is an error in creating client."""

    message = "Error to create a client."


class ClientGetItemException(BaseException):
    """Exception when there is an error to get a specific item."""

    message = "Error to get item of a client."


class ClientGetAllException(BaseException):
    """Exception when there is an error to get all the clients."""

    message = "Error to get all the clients."


class ClientFormatDataException(BaseException):
    """Exception when there is an error in format data."""

    message = "Error in format data client."
