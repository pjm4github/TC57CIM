from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketOpCommon.MktUserAttribute import MktUserAttribute
from IEC62325.MarketOperations.MarketSystem.MarketResults.MarketStatement import MarketStatement


class MarketStatementLineItem(IdentifiedObject):
    """
    An individual line item on an ISO settlement statement.
    @created 28-Dec-2023 8:23:32 PM
    """

    def __init__(self):
        # Current settlement amount.
        super().__init__()
        self.current_amount = 0.0

        # Current ISO settlement amount.
        self.current_iso_amount = 0.0

        # Current ISO settlement quantity.
        self.current_iso_quantity = 0.0

        # Current settlement price.
        self.current_price = 0.0

        # Current settlement quantity, subject to the UOM.
        self.current_quantity = 0.0

        # The date of which the settlement is run.
        self.interval_date = DateTime()

        # The number of intervals.
        self.interval_number = ""

        # Net settlement amount.
        self.net_amount = 0.0

        # Net ISO settlement amount.
        self.net_iso_amount = 0.0

        # Net ISO settlement quantity.
        self.net_iso_quantity = 0.0

        # Net settlement price.
        self.net_price = 0.0

        # Net settlement quantity, subject to the UOM.
        self.net_quantity = 0.0

        # Previous settlement amount.
        self.previous_amount = 0.0

        # Previous ISO settlement amount.
        self.previous_iso_amount = 0.0

        # Previous ISO settlement quantity.
        self.previous_iso_quantity = 0.0

        # Previous settlement price.
        self.previous_price = 0.0

        # Previous settlement quantity, subject to the UOM.
        self.previous_quantity = 0.0

        # The unit of measure for the quantity element of the line item.
        self.quantity_uom = ""

        self.container_market_statement_line_item = MarketStatementLineItem()
        self.market_statement = MarketStatement()
        self.mkt_user_attribute = MktUserAttribute()