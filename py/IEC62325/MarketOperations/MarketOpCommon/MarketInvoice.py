from IEC61970.Base.Domain.Date import Date
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Money import Money
from IEC62325.MarketOperations.MktDomain.MktAccountKind import MktAccountKind
from IEC62325.MarketOperations.MktDomain.MktBillMediaKind import MktBillMediaKind
from IEC62325.MarketOperations.ParticipantInterfaces.MajorChargeGroup import MajorChargeGroup

class MarketInvoice:
    #  * A roll up of invoice line items. The whole invoice has a due date and amount to
    #  * be paid, with information such as customer, banks etc. being obtained through
    #  * associations. The invoice roll up is based on individual line items that each
    #  * contain amounts and descriptions for specific services or products.
    #  * @created 27-Dec-2023 5:14:44 PM
    def __init__(self):
        self.amount = Money()  # Total amount due on this invoice based on line items and applicable adjustments.
        self.bill_media_kind = MktBillMediaKind.PAPER  # Kind of media by which the CustomerBillingInfo was delivered.
        self.due_date = Date()  # Calculated date upon which the Invoice amount is due.
        self.kind = MktAccountKind.ESTIMATE  # Kind of invoice (default is 'sales').
        self.mailed_date = Date()  # Date on which the customer billing statement/invoice was printed/mailed.
        self.pro_forma = False  # True if payment is to be paid by a Customer to accept a particular ErpQuote (with associated Design) and have work initiated, at which time an associated ErpInvoice should automatically be generated. EprPayment.subjectStatus satisfies terms specificed in the ErpQuote.
        self.reference_number = ""  # Number of an invoice to be reference by this invoice.
        self.transaction_date_time = DateTime()  # Date and time when the invoice is issued.
        self.transfer_type = ""  # Type of invoice transfer.
        self.major_charge_group = MajorChargeGroup()
