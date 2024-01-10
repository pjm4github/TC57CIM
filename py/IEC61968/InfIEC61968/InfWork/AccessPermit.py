# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.InfIEC61968.InfWork.WorkDocument import WorkDocument
from IEC61970.Base.Domain.Date import Date
from IEC61970.Base.Domain.Money import Money


class AccessPermit(WorkDocument):
    """
    A permit is sometimes needed to provide legal access to land or equipment. For
    example, local authority permission for road works.
    @created 29-Dec-2023 9:10:45 PM
    """

    def __init__(self) -> None:
        super().__init__()
        """
        Permit application number that is used by municipality, state, province, etc.
        """
        self.application_number: Optional[str] = ""

        """
        Date that permit became official.
        """
        self.effective_date: Optional[Date] = Date()

        """
        Permit expiration date.
        """
        self.expiration_date: Optional[Date] = Date()

        """
        Total cost of permit.
        """
        self.payment: Optional[Money] = Money()

        """
        Permit identifier.
        """
        self.permit_id: Optional[str] = ""


