#######################################################
# 
# BaseFrequency.py
# Python implementation of the Class BaseFrequency
# Generated by Enterprise Architect
# Created on:      25-Dec-2023 8:31:54 PM
# Original author: SELAOST1
# 
#######################################################
from IEC61970.Base.Domain.Frequency import Frequency
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject

class BaseFrequency(IdentifiedObject):
    """The class describe a base frequency for a power system network. In case of
    multiple power networks with different frequencies, e.g. 50 or 60 Hertz each
    network will have it's own base frequency class. Hence it is assumed that power
    system objects having different base frequencies appear in separate documents
    where each document has a single base frequency instance.
    """
    pass
