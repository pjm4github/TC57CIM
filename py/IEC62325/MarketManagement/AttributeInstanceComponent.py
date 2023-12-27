# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Local imports


from IEC62325.MarketManagement.TimeSeries import TimeSeries


class AttributeInstanceComponent:
    """
    A class used to provide information about an attribute.
    @author mspivbe2
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        """
        Constructor
        """
        # * The identification of the formal name of an attribute.
        self.attribute = ""
        # The instance value of the attribute.
        self.attribute_value = ""
        # A sequential value representing a relative sequence number.
        self.position = 0
        self.time_series = TimeSeries()
