#######################################################
# 
# Length.py
# Python implementation of the Class Length
# Generated by Enterprise Architect
# Created on:      16-Dec-2023 11:12:20 PM
# 
#######################################################
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Length:
    """Unit of length. Never negative.
    """

    def __init__(self, value=None) -> None:
        self.multiplier: UnitMultiplier = UnitMultiplier.none
        self.value: float = 0.0 if not value else value
        self.unit = UnitSymbol.M
