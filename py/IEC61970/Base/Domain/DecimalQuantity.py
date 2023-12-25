# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023
from decimal import Decimal
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Currency import Currency
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class DecimalQuantity:
    """
    Quantity with decimal value and associated unit or currency information.
    """

    def __init__(self) -> None:
        self.currency: Currency = Currency()
        self.multiplier: UnitMultiplier = UnitMultiplier.none
        self.unit: UnitSymbol = UnitSymbol.none
        self.value: Decimal = Decimal(0)

