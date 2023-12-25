#######################################################
# 
# Temperature.py
# Python implementation of the Class Temperature
# Generated by Enterprise Architect
# Created on:      16-Dec-2023 11:27:46 PM
# 
#######################################################
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Temperature:
    """Value of temperature in degrees Celsius.
    """
    unit = UnitSymbol.degC

    def __init__(self):
        self.multiplier = UnitMultiplier.none
        self.value = 0.0