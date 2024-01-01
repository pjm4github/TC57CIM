# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023

from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketSystem.MarketResults.BillDeterminant import BillDeterminant


class ChargeComponent(IdentifiedObject):
    """A Charge Component is a list of configurable charge quality items to feed into
    settlement calculation and/or bill determinants.
    
    @created 28-Dec-2023 5:20:12 PM
    """
    def __init__(self):
        super().__init__()
        self.delete_statusOptional[str] = ""
        self.effective_dateOptional[DateTime] = DateTime()
        self.equationOptional[str] = ""
        self.messageOptional[str] = ""
        self.round_offOptional[str] = ""
        self.sum_Optional[str] = ""
        self.termination_dateOptional[DateTime] = DateTime()
        self.type_Optional[str] = ""
        self.bill_determinantsOptional[BillDeterminant] = BillDeterminant()