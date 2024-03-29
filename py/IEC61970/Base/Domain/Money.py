#######################################################
# 
# Money.py
# Python implementation of the Class Money
# Generated by Enterprise Architect
# Created on:      16-Dec-2023 11:12:00 PM
# 
#######################################################
from IEC61970.Base.Domain.Currency import Currency
from IEC61970.Base.Domain.UnitMultiplier import UnitMultiplier

class Money:
    """Amount of money.
    """

    def __init__(self, v=None):
        self.multiplier = UnitMultiplier.none
        self.value: float = v
        self.unit: Currency = Currency.USD
