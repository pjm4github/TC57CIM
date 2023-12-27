#######################################################
# 
# Pressure.py
# Python implementation of the Class Pressure
# Generated by Enterprise Architect
# Created on:      16-Dec-2023 11:24:39 PM
# 
#######################################################
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Pressure:
    """Pressure in Pascal.
    """
    unit = UnitSymbol.Pa
    def __init__(self):
        self.mulitplier = UnitMultiplier.none
        self.value = 0.0