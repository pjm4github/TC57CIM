from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class ActivePowerChangeRate:
    def __init__(self):
        self.multiplier = UnitMultiplier.none  # The unit multiplier for the active power change rate value
        self.value: float = 0.0  # The numerical value of the active power change rate

    unit = UnitSymbol.WPers  # Static constant unit symbol for active power change rate
