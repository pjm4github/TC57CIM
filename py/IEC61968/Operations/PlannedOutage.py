# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106

from CIM_STD_PYTHON.TC57CIM.IEC61968.Operations.Outage import Outage


class PlannedOutage(Outage):
    
    def __init__(self):
        super().__init__()
        self.reason = ""
