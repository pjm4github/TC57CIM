#######################################################
# 
# PinBranchGroup.py
# Python implementation of the Class PinBranchGroup
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 6:37:31 PM
# Original author: sveinols
# 
#######################################################
from IEC61970.Base.OperationalLimits.BranchGroup import BranchGroup
from IEC61970.InfIEC61970.InfSIPS.GateInputPin import GateInputPin

class PinBranchGroup(GateInputPin):
    """Value associated with branch group is used as compare.
    """

    def __init__(self):
        super().__init__()
        self.branch_group = BranchGroup()
