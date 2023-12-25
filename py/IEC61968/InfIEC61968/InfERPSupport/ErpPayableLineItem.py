from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Status import Status
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpIdentifiedObject import ErpIdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpJournalEntry import ErpJournalEntry
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpPayable import ErpPayable
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpPayment import ErpPayment


class ErpPayableLineItem(ErpIdentifiedObject):

    def __init__(self):
        super().__init__()
        self.status = Status()
        self.erp_journal_entries = ErpJournalEntry()
        self.erp_payable = ErpPayable()
        self.erp_payments = ErpPayment()
