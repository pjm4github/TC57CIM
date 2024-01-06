from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.MarketOpCommon.MktMeasurement import MktMeasurement

class TiePoint(IdentifiedObject):
    """
    Site of an interface between interchange areas. The tie point can be a network
    branch (e.g., transmission line or transformer) or a switching device. For
    transmission lines, the interchange area boundary is usually at a designated
    point such as the middle of the line. Line end metering is then corrected for
    line losses.
    """
    def __init__(self):
        super().__init__()  # Call to the superclass's constructor
        self.tie_point_mw_rating = ActivePower()  # The MW rating of the tie point.
        self.for_mkt_measurement = MktMeasurement()  # A measurement is made on the A side of a tie point
        self.by_mkt_measurement = MktMeasurement()  # A measurement is made on the B side of a tie point
