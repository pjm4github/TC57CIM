# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class CapacitancePerLength:
    """
    Capacitance per unit of length.
    @author T. Kostic
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """

    unit: UnitSymbol = UnitSymbol.FPerm

    def __init__(self) -> None:
        self.value: float = 0.0

        self.multiplier: UnitMultiplier = UnitMultiplier.none
