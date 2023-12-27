# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.InfIEC61968.InfERPSupport.ErpDocument import ErpDocument
from IEC61968.InfIEC61968.InfERPSupport.ErpLedgerEntry import ErpLedgerEntry


class ErpLedger(ErpDocument):

    def __init__(self):
        super().__init__()
        self.erp_ledger_entries = ErpLedgerEntry()

