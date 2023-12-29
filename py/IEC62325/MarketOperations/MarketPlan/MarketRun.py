from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketPlan.Market import Market
from IEC62325.MarketOperations.MktDomain.ExecutionType import ExecutionType
from IEC62325.MarketOperations.MktDomain.MarketType import MarketType


class MarketRun(IdentifiedObject):
    def __init__(self):
        # The execution type; Day Ahead, Intra Day, Real Time Pre-Dispatch, Real Time Dispatch
        super().__init__()
        self.execution_type = ExecutionType.DA

        # Approved time for case. Identifies the time that the dispatcher approved a specific real time unit dispatch case
        self.market_approval_time = DateTime()

        # Set to true when the plan is approved by authority and becomes the official plan for the day ahead market.
        # Identifies the approved case for the market for the specified time interval.
        self.market_approved_status = False

        # The end time defined as the end of the market, market end time.
        self.market_end_time = DateTime()

        # The start time defined as the beginning of the market, market start time.
        self.market_start_time = DateTime()

        # The market type, Day Ahead Market or Real Time Market.
        self.market_type = MarketType.DAM

        # This is the state of market run activity as reported by market systems to the market definition services.
        self.reported_state = ""

        # This is the state controlled by market defintion service.
        # Possible values could be but not limited by: Open, Close.
        self.run_state = ""

        self.market = Market()
