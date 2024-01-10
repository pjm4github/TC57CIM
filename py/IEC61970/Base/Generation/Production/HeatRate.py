# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
# Class definition for HeatRate
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class HeatRate:
    """
    Heat generated, in energy per time unit of elapsed time.

    @created 02-Jan-2024 10:54:40 PM
    """

    def __init__(self, val=0.0):
        super().__init__()
        self.multiplier = UnitMultiplier.none  # Initialize multiplier to a UnitMultiplier class instance
        self.unit = UnitSymbol.J  # Initialize unit to UnitSymbol.J class attribute
        self.value = val  # Initialize value to a Float class instance
        # end HeatRate
