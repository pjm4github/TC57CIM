from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject  # Importing IdentifiedObject class from IEC61970.Base.Core module
from IEC62325.MarketOperations.ReferenceData.RTO import RTO  # Importing RTO class from IEC62325.MarketOperations.ReferenceData module

class ResourceGroupReq(IdentifiedObject):
    """
    Ancillary service requirements for a market.
    @created 28-Dec-2023 7:58:28 PM
    """

    def __init__(self):
        super().__init__()  # Calling the __init__() method of the superclass
        self.RTOs = RTO()  # Creating an instance of RTO class and assigning it to the 'RTOs' attribute
