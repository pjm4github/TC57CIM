from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Hours:
    """
    Number of hours
    """
    unit = UnitSymbol.none

    def __init__(self):
        self.multiplier = UnitMultiplier.none
        self.value = 0.0