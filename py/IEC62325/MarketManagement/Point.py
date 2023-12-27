# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC62325.MarketManagement.AceTariffType import AceTariffType
from IEC62325.MarketManagement.Period import Period
from IEC62325.MarketManagement.TimeSeries import TimeSeries


class Point:
    """
    An identification of a set of values beeing addressed within a specific interval
    of time.
    @author: effantin-cyr
    @version: 1.0
    @created: 25-Dec-2023 9:21:23 PM
    """

    def __init__(self):
        """
        Constructor
        """
        self.position = 0  # A sequential value representing the relative position within a given time interval
        self.quality = ""  # The quality of the information being provided. This quality may be estimated, not available, as provided, etc.
        self.quantity = 0  # Principal quantity identified for a point
        self.secondary_quantity = 0  # Secondary quantity identified for a point
        self.period = Period()
        self.time_series = TimeSeries()
        self.ace_tariff_type = AceTariffType()

