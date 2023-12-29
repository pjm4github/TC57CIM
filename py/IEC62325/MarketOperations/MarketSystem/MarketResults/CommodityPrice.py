# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from IEC62325.MarketOperations.MarketPlan.CommodityDefinition import CommodityDefinition
from IEC62325.MarketOperations.MarketSystem.MarketResults.PriceDescriptor import PriceDescriptor


class CommodityPrice:
    """
    The CommodityPrice class is used to define the price of a commodity during a
    given time interval. The interval may be long, e.g. a year, or very short, e.g.
    5 minutes. There will be many instances of the CommodityPrice class for each
    instance of the CommodityDefinition to which it is associated. Note that there
    may be more than once price associated with a given interval and these variances
    are described by the association (or associations) with the PriceDescriptor class.
    @author Margaret
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        """
        The time interval over which the CommodityPrice is valid, using the standard
        conventions associated with the DateTimeInterval class.
        """
        self.time_interval_period = DateTimeInterval()
        
        """
        The price of the Commodity, expressed as a floating point value with the
        currency and unit of measure defined in the associated CommodityDefinition
        class.
        """
        self.value = 0.0
        
        self.price_descriptor = PriceDescriptor()
        self.commodity_definition = CommodityDefinition()
