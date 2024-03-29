#######################################################
# 
# RemedialActionScheme.py
# Python implementation of the Class RemedialActionScheme
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 3:53:33 PM
# Original author: sveinols
# 
#######################################################
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61970.InfIEC61970.InfSIPS.Stage import Stage

class RemedialActionScheme(PowerSystemResource):
    """Remedial Action Scheme (RAS), Special Protection Schemes (SPS), System
    Protection Schemes (SPS) or System Integrity Protection Schemes (SIPS).
    """

    def __init__(self):
        super().__init__()
        self.stage = Stage()
