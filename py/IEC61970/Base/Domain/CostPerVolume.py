# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Currency import Currency

class CostPerVolume:

    def __init__(self) -> None:
        self.denominator_multiplier: UnitMultiplier = UnitMultiplier()
        self.denominator_unit: UnitSymbol = UnitSymbol.m3  # 'm3'
        self.multiplier: UnitMultiplier = UnitMultiplier.none
        self.unit: Currency = Currency()
        self.value: float = 0.0
