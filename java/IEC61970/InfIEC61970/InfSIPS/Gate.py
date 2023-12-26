#######################################################
# 
# Gate.py
# Python implementation of the Class Gate
# Generated by Enterprise Architect
# Created on:      25-Dec-2023 8:31:58 PM
# Original author: sveinols
# 
#######################################################
from IEC61970.InfIEC61970.InfSIPS.GateLogicKind import GateLogicKind
from IEC61970.InfIEC61970.InfSIPS.RemedialActionScheme import RemedialActionScheme
from IEC61970.InfIEC61970.InfSIPS.PinGate import PinGate
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.InfIEC61970.InfSIPS.GateInputPin import GateInputPin

class Gate(IdentifiedObject):
    """Logical gate than support logical operation based on the input.
    """
    RemedialActionScheme= RemedialActionScheme()

    PinGate= PinGate()

    GateInputPin= GateInputPin()
