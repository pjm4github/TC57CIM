# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Document import Document
from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.SwitchingPlan import SwitchingPlan
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class SwitchingOrder(Document):
    
    def __init__(self):
        super().__init__()
        self.comment = ""
        self.planned_execution_interval = DateTimeInterval()
        self.switching_plan = SwitchingPlan()
