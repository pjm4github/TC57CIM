# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpDocument import ErpDocument
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpTimeEntry import ErpTimeEntry


class ErpTimeSheet(ErpDocument):

    def __init__(self):
        super().__init__()
        self.erp_time_entries = ErpTimeEntry()
