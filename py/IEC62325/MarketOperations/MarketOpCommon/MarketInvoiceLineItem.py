from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval
from IEC62325.MarketOperations.MarketOpCommon.MarketInvoice import MarketInvoice
from IEC62325.MarketOperations.MktDomain.MktInvoiceLineItemKind import MktInvoiceLineItemKind
from IEC62325.MarketOperations.MarketSystem.MarketResults.Settlement import Settlement


class MarketInvoiceLineItem:
    """
    #  * An individual line item on an invoice.
    #  * @created 27-Dec-2023 5:14:58 PM
    """
    def __init__(self):
        self.bill_period = DateTimeInterval()  # Bill period for the line item.
        self.gl_account = ""  # General Ledger account code, shall be a valid combination.
        self.gl_date_time = DateTime()  # Date and time line item will be posted to the General Ledger.
        self.kind = MktInvoiceLineItemKind()  # Kind of line item.
        self.line_amount = 0.0  # Amount due for this line item.
        self.line_number = ""  # Line item number on invoice statement.
        self.line_version = ""  # Version number of the bill run.
        self.net_amount = 0.0  # Net line item charge amount.
        self.previous_amount = 0.0  # Previous line item charge amount.
        self.settlement = Settlement()
        self.container_market_invoice_line_item = MarketInvoiceLineItem()
        self.market_invoice = MarketInvoice()