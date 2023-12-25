#######################################################
# 
# Reactance.py
# Python implementation of the Class Reactance
# Generated by Enterprise Architect
# Created on:      16-Dec-2023 11:24:59 PM
# 
#######################################################
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class Reactance:
    """Reactance (imaginary part of impedance), at rated frequency.
    """
    unit = UnitSymbol.ohm

    def __init__(self):
        self.multiplier = UnitMultiplier.none
        self.value = 0.0