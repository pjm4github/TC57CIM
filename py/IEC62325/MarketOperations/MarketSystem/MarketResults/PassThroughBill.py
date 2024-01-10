from IEC61968.Common.Document import Document
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Money import Money
from IEC62325.MarketOperations.MarketOpCommon.MktUserAttribute import MktUserAttribute
from IEC62325.MarketOperations.MarketSystem.MarketResults.MarketStatementLineItem import MarketStatementLineItem


class PassThroughBill(Document):
    """
    Pass Through Bill is used for:
    1) Two sided charge transactions with or without ISO involvement
    2) Specific direct charges or payments that are calculated outside or provided directly to settlements
    3) Specific charge bill determinants that are externally supplied and used in charge calculations
    @created 28-Dec-2023 8:24:12 PM
    """

    def __init__(self):
        super().__init__()
        self.adjusted_amount = Money()

        # The charge amount of the product/service.
        self.amount = Money()

        # The company to which the PTB transaction is billed.
        self.billed_to = ""

        # Bill period end date
        self.bill_end = DateTime()

        # The settlement run type, for example: prelim, final, and rerun.
        self.bill_run_type = ""

        # Bill period start date
        self.bill_start = DateTime()

        # The effective date of the transaction
        self.effective_date = DateTime()

        # Disputed transaction indicator
        self.is_disputed = False

        # A flag indicating whether there is a profile data associated with the PTB.
        self.is_profiled = False

        # The company to which the PTB transaction is paid.
        self.paid_to = ""

        # The previous bill period end date
        self.previous_end = DateTime()

        # The previous bill period start date
        self.previous_start = DateTime()

        # The price of product/service.
        self.price = Money()

        # The product identifier for determining the charge type of the transaction.
        self.product_code = ""

        # The company by which the PTB transaction service is provided.
        self.provided_by = ""

        # The product quantity.
        self.quantity = 0.0

        # The end date of service provided, if periodic.
        self.service_end = DateTime()

        # The start date of service provided, if periodic.
        self.service_start = DateTime()

        # The company to which the PTB transaction is sold.
        self.sold_to = ""

        # The tax on services taken.
        self.tax_amount = Money()

        # The time zone code1
        self.time_zone = ""

        # The trade date
        self.trade_date = DateTime()

        # The date the transaction occurs.
        self.transaction_date = DateTime()

        # The type of transaction. For example, charge customer, bill customer, matching AR/AP, or bill determinant
        self.transaction_type = ""

        self.market_statement_line_item = MarketStatementLineItem()
        self.mkt_user_attribute = MktUserAttribute()