# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Location import Location
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.Incident import Incident
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class TroubleOrder(Document):
    
    def __init__(self):
        super().__init__()
        self.comment = ""
        self.planned_execution_interval = DateTimeInterval()
        self.incident = Incident()
        self.location = Location()
