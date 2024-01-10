#######################################################
# 
# VoltagePerReactivePower.py
# Python implementation of the Class VoltagePerReactivePower
# Generated by Enterprise Architect
# Created on:      16-Dec-2023 11:29:59 PM
# 
#######################################################
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class VoltagePerReactivePower:
    """
    Voltage variation with reactive power.
    """
    def __init__(self):
        self.multiplier = UnitMultiplier.none
        self.value = 0.0
        self.unit = UnitSymbol.VPerVAr
