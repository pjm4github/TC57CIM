from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Conductance:
    """Real part of admittance
    @author T. Kostic
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """

    def __init__(self) -> None:
        self.multiplier: UnitMultiplier = UnitMultiplier.none
        self.value: float = 0.0
        self.unit = UnitSymbol.S  # ureg('S')
