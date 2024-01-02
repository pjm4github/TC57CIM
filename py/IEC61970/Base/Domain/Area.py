# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023

from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Area:
    def __init__(self, v=0.0) -> None:
        self.multiplier: UnitMultiplier = UnitMultiplier.none
        self.value: float = v
        self.unit: UnitSymbol = UnitSymbol.m2

