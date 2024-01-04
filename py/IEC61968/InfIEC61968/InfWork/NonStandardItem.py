# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.InfIEC61968.InfWork.WorkDocument import WorkDocument
from IEC61970.Base.Domain.Money import Money


class NonStandardItem(WorkDocument):
    """
    This document provides information for non-standard items like customer
    contributions (e.g., customer digs trench), vouchers (e.g., credit), and
    contractor bids.
    @created 29-Dec-2023 9:16:53 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.amount: Optional[Money] = Money()  # The projected cost for this item.