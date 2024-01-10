# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Emission:
    """
    Quantity of emission per fuel heat content.
    @created 02-Jan-2024 10:52:37 PM
    """

    multiplier = UnitMultiplier.none  # Default value for multiplier
    unit = UnitSymbol.kg  # Default value for unit

    def __init__(self):
        super().__init__()
        self.value = 0.0  # Default value for value
