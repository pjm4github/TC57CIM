# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class ServiceMultiplier(IdentifiedObject):
    
    def __init__(self):
        super().__init__()
        self.kind = None  # Kind of multiplier.
        self.value = 1.0  # Multiplier value.
