from IEC61968.Common.Document import Document
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketOpCommon.MktActivityRecord import MktActivityRecord
from IEC62325.MarketOperations.MarketPlan.Market import Market


class MarketFactors(Document):
    """
    Aggregation of market information relative for a specific time interval.
    @created 28-Dec-2023 8:12:00 PM
    """

    def __init__(self):
        # The end of the time interval for which requirement is defined.
        super().__init__()
        self.interval_end_time = DateTime()

        # The start of the time interval for which requirement is defined.
        self.interval_start_time = DateTime()

        self.market = Market()
        self.mkt_activity_record = MktActivityRecord()