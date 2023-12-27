from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Hours:
    """
    Number of hours
    """
    unit = UnitSymbol.none

    def __init__(self):
        self.multiplier = UnitMultiplier.none
        self.value = 0.0