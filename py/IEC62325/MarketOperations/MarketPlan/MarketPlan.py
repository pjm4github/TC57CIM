from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketPlan.PlannedMarket import PlannedMarket


class MarketPlan(IdentifiedObject):
    """
    This class identifies a set of planned markets.
    @created 28-Dec-2023 8:12:12 PM
    """

    def __init__(self):
        # Planned market trading day.
        super().__init__()
        self.trading_day = DateTime()

        # A market plan has a number of markets (DA, HA, RT).
        self.planned_market = PlannedMarket()
