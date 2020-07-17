import re
from backend.exceptions.client_exceptions import ClientFormatDataException


class CheckClientDataFormat:
    """Check th Client Data Format"""

    def __init__(self, client_data: dict):
        """Check Client Data Format Init.

        **client_data:
        id: client id
        name: client name
        last_name: client last name
        identity_card: client identity card
        email: client email
        phone_1: client phone 1
        phone_2: client phone 2s
        address: client address.
        """

        # Check missing mandatory data
        CheckClientDataFormat.missing_mandatory_data(
            client_data=client_data
        )

        for key, value in client_data.items():
            if value:
                try:
                    if key == "identity_card":
                        self.identity_card(identity_card=value)
                    if key == "email":
                        self.email(email=value)
                    if key == "phone_1":
                        self.phone(phone=value)
                    if key == "phone_2":
                        self.phone(phone=value)
                except ClientFormatDataException as error:
                    raise ClientFormatDataException(message=error.message)

    @staticmethod
    def identity_card(identity_card: str):
        """Check identity card format."""
        pattern = "^[vVeE][-][0-9]{2}[0-9]{3}[0-9]{3}$"
        identity_card_format = re.compile(pattern)
        result = identity_card_format.match(identity_card)
        if not result:
            message = "Format identity card incorrect."
            raise ClientFormatDataException(message=message)

    @staticmethod
    def email(email: str):
        """Check email format."""
        pattern = "^[A-Za-z0-9]+[\._]?[A-Za-z0-9]+[@]\w+[.]\w{2,3}$"
        email_format = re.compile(pattern)
        result = email_format.match(email)
        if not result:
            message = "Format email incorrect."
            raise ClientFormatDataException(message=message)

    @staticmethod
    def phone(phone: str):
        """Check phone format."""
        pattern = "^[0-9]{4}[-][0-9]{7}$"
        phone_format = re.compile(pattern)
        result = phone_format.match(phone)
        if not result:
            message = "Format phone incorrect."
            raise ClientFormatDataException(message=message)

    @staticmethod
    def missing_mandatory_data(client_data: dict):
        """Missing Mandatory Data."""
        mandatory_data = ["name", "last_name", "identity_card", "address"]
        for key, value in client_data.items():
            if key in mandatory_data:
                if not value:
                    message = f"Missing Mandatory Data: {key}"
                    raise ClientFormatDataException(message=message)
