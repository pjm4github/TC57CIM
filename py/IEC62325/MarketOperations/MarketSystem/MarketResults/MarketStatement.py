from IEC61968.Common.Document import Document
from IEC61970.Base.Domain.DateTime import DateTime


class MarketStatement(Document):
    """
    A statement is a roll up of statement line items. Each statement along with its line items provide the details of specific charges at any given time. Used by Billing and Settlement.
    @created 28-Dec-2023 8:23:22 PM
    """

    def __init__(self):
        # The end of a bill period.
        super().__init__()
        self.end = DateTime()

        # The version number of previous statement (in the case of true up).
        self.reference_number = ""

        # The start of a bill period.
        self.start = DateTime()

        # The date of which Settlement is run.
        self.trade_date = DateTime()

        # The date of which this statement is issued.
        self.transaction_date = DateTime()