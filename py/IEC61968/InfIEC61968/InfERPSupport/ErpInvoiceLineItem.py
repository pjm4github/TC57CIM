# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.UserAttribute import UserAttribute
from IEC61968.InfIEC61968.InfERPSupport.ErpInvoice import ErpInvoice
from IEC61968.InfIEC61968.InfERPSupport.ErpInvoiceLineItemKind import ErpInvoiceLineItemKind
from IEC61968.InfIEC61968.InfERPSupport.ErpJournalEntry import ErpJournalEntry
from IEC61968.InfIEC61968.InfERPSupport.ErpPayableLineItem import ErpPayableLineItem
from IEC61968.InfIEC61968.InfERPSupport.ErpPayment import ErpPayment
from IEC61968.InfIEC61968.InfERPSupport.ErpRecLineItem import ErpRecLineItem
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class ErpInvoiceLineItem:

    def __init__(self):
        self.bill_period = DateTimeInterval()
        self.gl_account = ""
        self.gl_date_time = DateTime()
        self.kind = ErpInvoiceLineItemKind.RECALCULATION
        self.line_amount = 0.0
        self.line_number = ""
        self.line_version = ""
        self.net_amount = 0.0
        self.previous_amount = 0.0
        self.erp_journal_entries = ErpJournalEntry()
        self.container_erp_invoice_line_item = ErpInvoiceLineItem()
        self.erp_rec_line_item = ErpRecLineItem()
        self.erp_payments = ErpPayment()
        self.erp_invoice = ErpInvoice()
        self.erp_payable_line_item = ErpPayableLineItem()
        self.user_attributes = UserAttribute()
