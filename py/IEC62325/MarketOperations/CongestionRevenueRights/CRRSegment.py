from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Money import Money


class CRRSegment(IdentifiedObject):
    """
    CRRSegment represents a segment of a CRR in a particular time frame.

    The segment class contains amount, clearing price, start date and time, end
    date and time.
    """

    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.amount = Money()  # Dollar amount = quantity x clearingPrice
        self.clearing_price = Money()  # Clearing price of a CRR
        self.end_date_time = DateTime()  # segment end date time
        self.quantity = 1.0  # The MW amount associated with the CRR
        self.start_date_time = DateTime()  # segment start date time
