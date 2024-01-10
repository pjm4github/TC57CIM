# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local import
from IEC61970.Base.Core.RegularIntervalSchedule import RegularIntervalSchedule
from IEC62325.MarketOperations.ParticipantInterfaces.ProductBid import ProductBid


class BidHourlyProductSchedule(RegularIntervalSchedule):
    """
    Containment for bid parameters that are dependent on a market product type.
    @author mspivbe2
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        super().__init__()
        self.product_bid = ProductBid()

