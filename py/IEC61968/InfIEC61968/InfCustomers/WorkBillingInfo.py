# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:39:47 2023
from IEC61968.Common.Document import Document
from IEC61968.InfIEC61968.InfERPSupport.ErpInvoiceLineItem import ErpInvoiceLineItem
from IEC61968.InfIEC61968.InfWork.NonStandardItem import Money
from IEC61968.Work.Work import Work
from IEC61970.Base.Domain.DateTime import DateTime


class WorkBillingInfo(Document):
    """
    Billing information for work performed for the customer. The history of Work
    Billing Info, Invoices, and Payments is to be maintained in associated
    Activity Records.
    @created 29-Dec-2023 9:26:25 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.cost_estimate: Money = Money(0)  # Estimated cost for work
        self.deposit: Money = Money(0)  # Amount of price on deposit
        self.discountfloat = 0.0  # Discount from standard price
        self.due_date_time: DateTime = DateTime()  # Date and time by which payment for bill is expected from client
        self.issue_date_time: DateTime = DateTime()  # Date and time bill was issued to client
        self.received_date_time = DateTime()  # Date payment was received from client
        self.work_price = Money(0)  # Amount of bill
        self.erp_line_items = ErpInvoiceLineItem()
        self.works = Work()
