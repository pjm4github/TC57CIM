#######################################################
# 
# Hazard.py
# Python implementation of the Class Hazard
# Generated by Enterprise Architect
# Created on:      19-Dec-2023 1:11:17 PM
# 
#######################################################
from IEC61968.Common.Status import Status
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class Hazard(IdentifiedObject):
    """An object or a condition that is a danger for causing loss or perils to an
    asset and/or people.
    """
    def __init__(self):
        super().__init__()
        self.status = Status()
        self.type = ""