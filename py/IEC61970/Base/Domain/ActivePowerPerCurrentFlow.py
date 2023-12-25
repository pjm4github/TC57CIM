# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class ActivePowerPerCurrentFlow:
    unit = UnitSymbol.none

    def __init__(self):
        self.multiplier = UnitMultiplier.none
        self.value: float = 0.0

