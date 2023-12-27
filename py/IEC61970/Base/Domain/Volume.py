#######################################################
# 
# Volume.py
# Python implementation of the Class Volume
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 12:07:57 AM
# 
#######################################################
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Volume:
    """Volume.
    """
    unit = UnitSymbol.m3

    def __init__(self):
        self.multiplier = UnitMultiplier.none
        self.value = 0.0