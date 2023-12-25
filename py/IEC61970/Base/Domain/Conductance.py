from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol

class Conductance:
    """Real part of admittance
    @author T. Kostic
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """
    unit = UnitSymbol.S  # ureg('S')
    def __init__(self) -> None:
        self.multiplier: UnitMultiplier = UnitMultiplier.none
        self.value: Optional[float] = 0.0
