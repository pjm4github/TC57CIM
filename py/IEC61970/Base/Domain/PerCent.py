#######################################################
# 
# PerCent.py
# Python implementation of the Class PerCent
# Generated by Enterprise Architect
# Created on:      16-Dec-2023 11:24:18 PM
# 
#######################################################
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class PerCent:
    """Percentage on a defined base.   For example, specify as 100 to indicate at the
    defined base.
    """
    unit = UnitSymbol.none

    def __init__(self):
        self.multiplier = UnitMultiplier.none
        self.value = 0.0
