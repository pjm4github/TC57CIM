# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.MarketManagement.Domain import Domain
from IEC62325.MarketManagement.Point import Point
from IEC62325.MarketManagement.TimeSeries import TimeSeries


class Price:
    """
    The cost corresponding to a specific measure and expressed in a currency.
    @author effantin-cyr
    @version 1.0
    @created 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        """
        A number of monetary units specified in a unit of currency.
        """
        self.amount = 0.0

        """
        The category of a price to be used in a price calculation. The price category
        is mutually agreed between System Operators.
        """
        self.category = ""

        """
        The direction indicates whether a System Operator pays the Market Parties or
        inverse.
        """
        self.direction = ""

        self.point = Point()
        self.time_series = TimeSeries()
        self.domain = Domain()
