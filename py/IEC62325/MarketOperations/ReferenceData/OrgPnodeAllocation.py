# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC62325.MarketOperations.ReferenceData.Pnode import Pnode


class OrgPnodeAllocation(IdentifiedObject):
    """
    This class models the allocation between asset owners and pricing nodes.
    @created 28-Dec-2023 12:18:45 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.max_mw_allocation: ActivePower = ActivePower()
        self.pnode: Pnode = Pnode()

