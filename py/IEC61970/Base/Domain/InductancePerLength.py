# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023
# from IEC61970.Base.Domain import UnitMultiplier, UnitSymbol
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class InductancePerLength:
    """Inductance per unit of length.
    """

    def __init__(self) -> None:
        self.multiplier: UnitMultiplier = UnitMultiplier.none
        self.value: float = 0.0
        self.unit = UnitSymbol.HPerm
