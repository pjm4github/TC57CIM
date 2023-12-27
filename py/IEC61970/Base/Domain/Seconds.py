#######################################################
# 
# Seconds.py
# Python implementation of the Class Seconds
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 9:51:35 PM
# 
#######################################################
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol

class Seconds:
    """Time, in seconds.
    """
    unit = UnitSymbol.s

    def __init__(self):
        self.value = 0.0
        self.multiplier = UnitMultiplier.none
