# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from typing import Optional

from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class ISOAPAddressing:

    def __init__(self) -> None:
        self.multiplier: UnitMultiplier = UnitMultiplier.none
        self.value: Optional[str] = ""
        self.unit = UnitSymbol.none
