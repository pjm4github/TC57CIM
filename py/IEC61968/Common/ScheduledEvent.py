# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.Asset import Asset
from CIM_STD_PYTHON.TC57CIM.IEC61968.Common.Status import Status
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Seconds import Seconds


class ScheduledEvent(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.duration = Seconds()
        self.status = Status()
        self.type = ""
        self.assets = Asset()
