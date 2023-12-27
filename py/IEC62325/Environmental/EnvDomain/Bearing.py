# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local imports
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Bearing:
    # The bearing in degrees (with 360 degrees being True North). Measured in
    # degrees clockwise from True North. 0 degrees indicates no direction being
    # given.
    # @author mcmorran
    # @version 1.0
    # @created 25-Dec-2023 9:21:22 PM

    def __init__(self):
        self.multiplier = UnitMultiplier.none
        self.unit = UnitSymbol.deg
        self.value = 0.0

