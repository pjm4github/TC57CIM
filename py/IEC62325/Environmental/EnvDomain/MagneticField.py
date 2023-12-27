# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class MagneticField:
    """
    * Magnetic field in nanotesla.
    * @author ppbr003
    * @version 1.0
    * @created 25-Dec-2023 9:21:22 PM
    """

    def __init__(self):
        pass
        self.multiplier = UnitMultiplier.n
        self.unit = UnitSymbol.T
        self.value = None