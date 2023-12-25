# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Status import Status
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpIdentifiedObject import ErpIdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpPOLineItem import ErpPOLineItem
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpRequisition import ErpRequisition
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Money import Money


class ErpReqLineItem(ErpIdentifiedObject):

    def __init__(self):
        super().__init__()
        self.code = ""
        self.cost = Money()
        self.delivery_date = Date()
        self.quantity = 0
        self.status = Status()
        self.erp_po_line_item = ErpPOLineItem()
        self.erp_requisition = ErpRequisition()
