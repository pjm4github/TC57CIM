#######################################################
# 
# CurrentFlow.py
# Python implementation of the Class Currency
# Generated by Enterprise Architect
# Created on:      16-Dec-2023 9:54:21 PM
# 
#######################################################
from IEC61970.Base.Domain.UncefactUnitCode import UncefactUnitCode
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier
from IEC61970.Base.Domain.UnitSymbol import UnitSymbol


class CurrentFlow:
    """
    Electrical current with sign convention: positive flow is out of the conducting equipment
    into the connectivity node. Can be both AC and DC.
    """

    def __init__(self):
        self.multiplier = UnitMultiplier.none  # The unit multiplier for the current value
        self.uncefact_unit_code = UncefactUnitCode()  # The UN/CEFACT unit code1 for the voltage value
        self.value: float = 0.0  # The numerical value of the current
        self.unit = UnitSymbol.A  # Static constant unit symbol for current
