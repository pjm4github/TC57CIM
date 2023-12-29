# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource
from IEC62325.MarketManagement.TimeSeries import TimeSeries


class MarketObjectStatus:
    """
    The condition or position of an object with regard to its standing.
    @author mspivbe2
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        """
        The coded condition or position of an object with regard to its standing.
        """
        self.status = ""
        self.time_series = TimeSeries()
        self.registered_resource = RegisteredResource()
