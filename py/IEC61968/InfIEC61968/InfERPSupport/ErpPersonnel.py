# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Status import Status
from CIM_STD_PYTHON.TC57CIM.IEC61968.InfIEC61968.InfERPSupport.ErpIdentifiedObject import ErpIdentifiedObject


class ErpPersonnel(ErpIdentifiedObject):

    def __init__(self):
        super().__init__()
        self.status = Status()