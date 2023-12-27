# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfERPSupport.ErpIdentifiedObject import ErpIdentifiedObject
from IEC61968.InfIEC61968.InfERPSupport.ErpInvoiceLineItem import ErpInvoiceLineItem
from IEC61968.InfIEC61968.InfERPSupport.ErpPOLineItem import ErpPOLineItem
from IEC61968.InfIEC61968.InfERPSupport.ErpReceiveDelivery import ErpReceiveDelivery


class ErpRecDelvLineItem(ErpIdentifiedObject):

    def __init__(self):
        super().__init__()
        self.status = Status()
        self.erp_receive_delivery = ErpReceiveDelivery()
        self.erp_po_line_item = ErpPOLineItem()
        self.erp_invoice_line_item = ErpInvoiceLineItem()
