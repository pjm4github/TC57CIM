# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.Metering.UsagePoint import UsagePoint
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class UsagePointGroup(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.type = ""
        self.usage_points = UsagePoint()
