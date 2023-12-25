#######################################################
# 
# WaterLevel.py
# Python implementation of the Class WaterLevel
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 12:08:23 AM
# 
#######################################################
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class WaterLevel:
    """Reservoir water level referred to a given datum such as mean sea level.
    """
    unit = UnitSymbol.m

    def __init__(self):
        self.multiplier = UnitMultiplier.none
        self.value = 0.0