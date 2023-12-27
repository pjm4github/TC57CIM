# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfERPSupport.ErpIdentifiedObject import ErpIdentifiedObject
from IEC61968.InfIEC61968.InfERPSupport.ErpJournalEntry import ErpJournalEntry
from IEC61968.InfIEC61968.InfERPSupport.ErpPayment import ErpPayment
from IEC61968.InfIEC61968.InfERPSupport.ErpReceivable import ErpReceivable


class ErpRecLineItem(ErpIdentifiedObject):

    def __init__(self):
        super().__init__()
        self.status = Status()
        self.erp_journal_entries = ErpJournalEntry()
        self.erp_receivable = ErpReceivable()
        self.erp_payments = ErpPayment()
