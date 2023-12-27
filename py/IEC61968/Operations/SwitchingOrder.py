# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Common.Document import Document
from IEC61968.Operations.SwitchingPlan import SwitchingPlan
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class SwitchingOrder(Document):
    
    def __init__(self):
        super().__init__()
        self.comment = ""
        self.planned_execution_interval = DateTimeInterval()
        self.switching_plan = SwitchingPlan()
