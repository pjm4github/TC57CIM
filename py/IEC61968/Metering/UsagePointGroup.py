# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Metering.UsagePoint import UsagePoint
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class UsagePointGroup(IdentifiedObject):

    def __init__(self):
        super().__init__()
        self.type = str()
        self.usage_points = UsagePoint()
