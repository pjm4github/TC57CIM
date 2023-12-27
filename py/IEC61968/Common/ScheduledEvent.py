# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Assets.Asset import Asset
from IEC61968.Common.Status import Status
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.Seconds import Seconds


class ScheduledEvent(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.duration = Seconds()
        self.status = Status()
        self.type = ""
        self.assets = Asset()
