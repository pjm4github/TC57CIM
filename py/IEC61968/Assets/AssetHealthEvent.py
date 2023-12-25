# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Duration import Duration
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.ActivityRecord import ActivityRecord

class AssetHealthEvent(ActivityRecord):
    
    def __init__(self):
        super().__init__()
        self.action_recommendation = ""
        self.action_timeline = Duration()
        self.effective_date_time = DateTime()
