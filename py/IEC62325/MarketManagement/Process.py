from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketManagement.MarketDocument import MarketDocument


class Process(IdentifiedObject):
    """
    The formal specification of a set of business transactions having the same
    business goal.
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.classification_type = str()  # The classification mechanism used within a business process.
        self.process_type = str()  # The kind of business process.
        self.market_document = MarketDocument()  # Associated MarketDocument
