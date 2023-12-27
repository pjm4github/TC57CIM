# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfERPSupport.ErpIdentifiedObject import ErpIdentifiedObject
from IEC61968.InfIEC61968.InfERPSupport.ErpProjectAccounting import ErpProjectAccounting


class ErpTimeEntry(ErpIdentifiedObject):

    def __init__(self):
        super().__init__()
        self.status = Status()
        self.erp_project_accounting = ErpProjectAccounting()
