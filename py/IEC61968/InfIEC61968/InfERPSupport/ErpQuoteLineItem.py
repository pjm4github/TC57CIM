# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfERPSupport.ErpInvoiceLineItem import ErpInvoiceLineItem
from IEC61968.InfIEC61968.InfERPSupport.ErpQuote import ErpQuote
from IEC61968.InfIEC61968.InfERPSupport.ErpReqLineItem import ErpReqLineItem


class ErpQuoteLineItem:

    def __init__(self):
        self.status = Status()
        self.erp_req_line_item = ErpReqLineItem()
        self.erp_invoice_line_item = ErpInvoiceLineItem()
        self.erp_quote = ErpQuote()
        self.design = Design()
