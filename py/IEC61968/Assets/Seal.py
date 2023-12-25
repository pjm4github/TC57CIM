# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.SealConditionKind import SealConditionKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.SealKind import SealKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime


class Seal(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.applied_date_time = DateTime()
        self.condition = SealConditionKind.OTHER
        self.kind = SealKind.STEEL
        self.seal_number = ""
