#######################################################
# 
# TriggerCondition.py
# Python implementation of the Class TriggerCondition
# Generated by Enterprise Architect
# Created on:      25-Dec-2023 8:32:04 PM
# Original author: sveinols
# 
#######################################################
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.InfSIPS.RemedialActionScheme import RemedialActionScheme
from IEC61970.InfIEC61970.InfSIPS.Gate import Gate

class TriggerCondition(IdentifiedObject):
    """A conditions that can trigger remedial actions.
    """
    RemedialActionScheme= RemedialActionScheme()

    GateTrigger= Gate()
