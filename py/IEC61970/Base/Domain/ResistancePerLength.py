# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023
from decimal import Decimal
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier


class ResistancePerLength:
    """
    Resistance (real part of impedance) per unit of length.
    @author T. Kostic
    @version 1.0
    @created 15-Dec-2023 4:38:29 PM
    """

    unit = UnitSymbol.ohmPerm

    def __init__(self) -> None:
        self.value: Optional[Decimal] = Decimal(0.0)
        self.multiplier = UnitMultiplier.none
