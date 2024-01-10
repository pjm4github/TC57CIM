# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.MarketOperations.MktDomain.MarketType import MarketType
from IEC62325.MarketOperations.MktDomain.PriceTypeKind import PriceTypeKind


class PriceDescriptor:
    # The price of a commodity during a given time interval may change over time.
    # For example, a price may be forecasted a year ahead, a month ahead, a day ahead,
    # an hour ahead, and in real time; this is defined using the MarketType.
    # Additionally, a price may have one or more components. For example, a locational
    # marginal energy price may be the arithmetic sum of the system price, the
    # congestion price, and the loss price. The priceType enumeration is used
    # to determine if the price is the complete price (priceType="total") or one of
    # potentially many constituent components.
    # Author: Margaret
    # Version: 1.0
    # Created: 25-Dec-2023 9:21:23 PM

    def __init__(self):
        pass
        # The time frame for the price, using the standard conventions associated with
        # the MarketType enumeration.
        self.market_type = MarketType.RTM

        # The "kind" of price being described. In general, the priceType will either be
        # "total" to signify that the price is the price paid to buy or sell the
        # commodity, sometimes referred to as an "all-in" price, or one of potentially
        # many components.
        self.price_type = PriceTypeKind.SYSTEM
