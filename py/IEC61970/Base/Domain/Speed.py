# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Speed:
    """Distance per unit of time.
    """

    def __init__(self) -> None:
        self.multiplier = UnitMultiplier.none
        self.value: float = 0.0
        self.unit = UnitSymbol.mPers
