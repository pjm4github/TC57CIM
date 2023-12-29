from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime


class Market(IdentifiedObject):
    """
    Market (e.g. Day Ahead Market, Real Time Market) with a description of the Market operation control parameters.
    @created 28-Dec-2023 8:11:35 PM
    """

    def __init__(self):
        # Market ending time - actual market end
        super().__init__()
        self.actual_end = DateTime()

        # Market starting time - actual market start
        self.actual_start = DateTime()

        # True if daylight savings time (DST) is in effect.
        self.dst = False

        # Market end time.
        self.end = DateTime()

        # Local time zone.
        self.local_time_zone = ""

        # Market start time.
        self.start = DateTime()

        # Market Status ('OPEN', 'CLOSED', 'CLEARED', 'BLOCKED')
        self.status = ""

        # Trading time interval length.
        self.time_interval_length = 0.0

        # Market trading date
        self.trading_day = DateTime()

        # Trading period that describes the market, possibilities could be for an Energy Market: Day, Hour
        # For a CRR Market: Year, Month, Season
        self.trading_period = ""