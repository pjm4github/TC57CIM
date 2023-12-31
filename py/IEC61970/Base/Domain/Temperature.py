#######################################################
# 
# Temperature.py
# Python implementation of the Class Temperature
# Generated by Enterprise Architect
# Created on:      16-Dec-2023 11:27:46 PM
# 
#######################################################
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Temperature:
    """
    Value of temperature in degrees Celsius.
    """

    def __init__(self, v=0.0):
        self.multiplier = UnitMultiplier.none
        self.value = v
        self.unit = UnitSymbol.degC
