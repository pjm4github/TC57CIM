# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Date import Date


class LifecycleDate:
    
    def __init__(self):
        self.installation_date = Date()
        self.manufactured_date = Date()
        self.purchase_date = Date()
        self.received_date = Date()
        self.removal_date = Date()
        self.retired_date = Date()
