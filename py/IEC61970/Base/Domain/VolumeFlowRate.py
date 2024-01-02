# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023
from enum import Enum
from typing import Optional

from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class VolumeFlowRate:

    def __init__(self, v=0.0) -> None:
        self.multiplier: UnitMultiplier = UnitMultiplier.none
        self.value: float = v
        self.unit: UnitSymbol = UnitSymbol.m3Pers
