# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local imports
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from IEC61970.Base.Domain.Duration import Duration
from IEC62325.MarketManagement.Reason import Reason


class Period:
    # An identification of a time interval that may have a given resolution.
    # @author effantin-cyr
    # @version 1.0
    # @created 25-Dec-2023 9:21:23 PM

    def __init__(self):
        pass
        # The number of units of time that compose an individual step within a period.
        self.resolution = Duration()

        # The start and end date and time for a given interval.
        self.time_interval = DateTimeInterval()

        self.reason = Reason()