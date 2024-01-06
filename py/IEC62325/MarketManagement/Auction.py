from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketManagement.TimeSeries import TimeSeries

class Auction(IdentifiedObject):
    """
    A class providing the identification and type of an auction.
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.allocation_mode = str()  # Identification of the method of allocation in an auction.
        self.cancelled = str()  # An indicator that signifies that the auction has been cancelled.
        self.category = str()  # The product category of an auction.
        self.payment_terms = str()  # The terms which dictate the determination of the bid payment price.
        self.rights = str()  # The rights of use the transmission capacity acquired in an auction.
        self.type = str()  # The kind of the Auction (e.g. implicit, explicit ...).
        self.time_series = TimeSeries()  # Associated TimeSeries object
