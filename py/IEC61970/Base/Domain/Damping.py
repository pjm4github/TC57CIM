
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Damping:
    #  * Per-unit active power variation with frequency referenced on the system
    #  * apparent power base. Typical values are in range 1.0 - 2.0.
    #  * @created 20-Dec-2023 6:19:16 PM
    def __init__(self):
        self.multiplier = UnitMultiplier  # Damping multiplier
        self.unit = UnitSymbol.onePerHz  # Damping unit
        self.value = 1.0  # Damping value
