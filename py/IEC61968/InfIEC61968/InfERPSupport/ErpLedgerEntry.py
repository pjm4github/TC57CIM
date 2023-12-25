# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Status import Status
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpAccountKind import ErpAccountKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpIdentifiedObject import ErpIdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpJournalEntry import ErpJournalEntry
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpLedBudLineItem import ErpLedBudLineItem
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Money import Money


class ErpLedgerEntry(ErpIdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.account_id = ""
        self.account_kind = ErpAccountKind()
        self.amount = Money()
        self.posted_date_time = DateTime()
        self.status = Status()
        self.transaction_date_time = DateTime()
        self.erp_journal_entry = ErpJournalEntry()
        self.erp_ledger_entry = ErpLedBudLineItem()
        self.user_attributes = UserAttribute()
