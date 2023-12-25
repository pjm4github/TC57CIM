# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Minutes import Minutes


class EndDeviceAction:
    
    def __init__(self):
        self.command = ""
        self.duration = Minutes()
        self.duration_indefinite = False
        self.start_date_time = DateTime()
