from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Minutes:
    """
    /**
     * Time in minutes.
     * @created 20-Dec-2023 6:20:37 PM
     */
    """
    def __init__(self):
        self. multiplier = UnitMultiplier.none
        self.unit = UnitSymbol.min
        self.value = 0.0
