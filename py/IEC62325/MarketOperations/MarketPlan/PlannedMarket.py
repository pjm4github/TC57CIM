from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketPlan.MarketRun import MarketRun
from IEC62325.MarketOperations.MarketPlan.PlannedMarketEvent import PlannedMarketEvent
from IEC62325.MarketOperations.MktDomain.MarketType import MarketType



class PlannedMarket:
    def __init__(self):
        # Market end time.
        self.market_end_time = DateTime()

        # Market start time.
        self.market_start_time = DateTime()

        # Market type.
        self.market_type = MarketType.DAM

        # A planned market could have multiple market runs for the reason that a planned market could have a rerun.
        self.market_run = MarketRun()

        # A planned market shall have a set of planned events
        self.planned_market_event = PlannedMarketEvent()
