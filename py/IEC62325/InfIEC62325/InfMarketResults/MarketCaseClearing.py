from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors


class MarketCaseClearing(MarketFactors):
    """
    Market case clearing results are posted for a given settlement period.
    @created 28-Dec-2023 8:01:56 PM
    """
    def __init__(self):
        # Settlement period:
        # 'DA - Bid-in'
        # 'DA - Reliability'
        # 'DA - Amp1'
        # 'DA - Amp2'
        # 'RT - Ex-Ante'
        # 'RT - Ex-Post'
        # 'RT - Amp1'
        # 'RT - Amp2'
        super().__init__()
        self.case_type = ""

        # Last time and date clearing results were manually modified.
        self.modified_date = DateTime()

        # Bid clearing results posted time and date.
        self.posted_date = DateTime()
