# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Jan  7 12:46:14 2024
# Cost, in units of currency, per quantity of heat generated.
# @created 02-Jan-2024 10:52:23 PM
from IEC61970.Base.Domain.Currency import Currency
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class CostPerHeatUnit:

    def __init__(self):
        super().__init__()
        self.denominator_multiplier = UnitMultiplier.none  # None
        self.denominator_unit = UnitSymbol.J  # None
        self.multiplier = UnitMultiplier.none  # assumed to be initialized with default values
        self.unit = Currency()  # assumed to be initialized with default values
        self.value = 0.0  # None
