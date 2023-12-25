from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Currency import Currency
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class CostPerEnergyUnit:
    #  * Cost, in units of currency, per quantity of electrical energy generated.
    def __init__(self):
        self.denominator_multiplier = UnitMultiplier.none  # Cost per energy unit denominator multiplier
        self.denominator_unit = UnitSymbol.Wh  # Cost per energy unit denominator unit
        self.multiplier = UnitMultiplier  # Cost per energy unit multiplier
        self.unit = Currency  # Cost per energy unit currency
        self.value = 0.0  # Cost per energy unit value
