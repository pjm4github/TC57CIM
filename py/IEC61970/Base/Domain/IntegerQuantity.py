
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class IntegerQuantity:
    #  * Quantity with integer value and associated unit information.
    #  * @created 20-Dec-2023 6:20:11 PM
    def __init__(self):
        self.multiplier = UnitMultiplier.none  # Integer quantity multiplier
        self.unit = UnitSymbol.count  # Integer quantity unit
        self.value = 0.0  # Integer quantity value
