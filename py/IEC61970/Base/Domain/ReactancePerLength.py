# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class ReactancePerLength:
    """
    Reactance (imaginary part of impedance) per unit of length, at rated frequency.
    """
    unit: UnitSymbol = UnitSymbol.ohmPerm

    def __init__(self) -> None:
        self.multiplier: UnitMultiplier = UnitMultiplier.none
        self.value: Optional[float] = 0.0
