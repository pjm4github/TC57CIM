#######################################################
# 
# PinTerminal.py
# Python implementation of the Class PinTerminal
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 6:40:53 PM
# Original author: sveinols
# 
#######################################################
from IEC61970.Base.Core.Terminal import Terminal
from IEC61970.InfIEC61970.InfSIPS.GateInputPin import GateInputPin

class PinTerminal(GateInputPin):
    """Value associated with Terminal is used as compare.
    """

    def __init__(self):
        super().__init__()
        self.terminal = Terminal()