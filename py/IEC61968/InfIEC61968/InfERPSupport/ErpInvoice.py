# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.InfIEC61968.InfERPSupport.BillMediaKind import BillMediaKind
from IEC61968.InfIEC61968.InfERPSupport.ErpDocument import ErpDocument
from IEC61968.InfIEC61968.InfERPSupport.ErpInvoiceKind import ErpInvoiceKind
from IEC61970.Base.Domain.Date import Date
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Money import Money


class ErpInvoice(ErpDocument):
    
    def __init__(self):
        super().__init__()
        self.amount = Money()
        self.bill_media_kind = BillMediaKind.PAPER
        self.due_date = Date()
        self.kind = ErpInvoiceKind.SALE
        self.mailed_date = Date()
        self.pro_forma = True
        self.reference_number = ""
        self.transaction_date_time = DateTime()
        self.transfer_type = ""
