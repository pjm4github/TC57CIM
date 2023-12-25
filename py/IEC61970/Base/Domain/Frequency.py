#######################################################
# 
# Frequency.py
# Python implementation of the Class Frequency
# Generated by Enterprise Architect
# Created on:      16-Dec-2023 10:55:21 PM
# 
#######################################################
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Frequency:
    """
    Cycles per second.
    """
    unit = UnitSymbol.Hz

    def __init__(self):
        self.multiplier = UnitMultiplier.none
        self.value = 0.0