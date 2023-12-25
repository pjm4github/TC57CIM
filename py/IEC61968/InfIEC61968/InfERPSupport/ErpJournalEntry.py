# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Status import Status
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpIdentifiedObject import ErpIdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Money import Money


class ErpJournalEntry(ErpIdentifiedObject):

    def __init__(self):
        super().__init__()
        self.account_id = ""
        self.amount = Money()
        self.posting_date_time = DateTime()
        self.source_id = ""
        self.status = Status()
        self.transaction_date_time = DateTime()
