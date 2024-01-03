# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from datetime import date
from typing import Optional

class AccessPermit(WorkDocument):
    """
    A permit is sometimes needed to provide legal access to land or equipment. For
    example, local authority permission for road works.
    @created 29-Dec-2023 9:10:45 PM
    """

    def __init__(self) -> None:
        """
        Permit application number that is used by municipality, state, province, etc.
        """
        self.application_numberOptional[str] = None

        """
        Date that permit became official.
        """
        self.effective_dateOptional[date] = None

        """
        Permit expiration date.
        """
        self.expiration_dateOptional[date] = None

        """
        Total cost of permit.
        """
        self.paymentOptional[Money] = None

        """
        Permit identifier.
        """
        self.permit_idOptional[str] = None
