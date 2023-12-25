# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class ConductancePerLength:
    """Real part of admittance per unit of length.
    @author T. Kostic
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """
    unit = UnitSymbol.SPerm  # ureg('S/m')
    def __init__(self) -> None:
        self.multiplier: UnitMultiplier = UnitMultiplier.none
        self.value: Optional[float] = 0.0
