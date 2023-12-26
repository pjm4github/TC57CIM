#######################################################
# 
# AnalogLimitSet.py
# Python implementation of the Class AnalogLimitSet
# Generated by Enterprise Architect
# Created on:      25-Dec-2023 8:31:54 PM
# 
#######################################################
from IEC61970.Base.Meas.LimitSet import LimitSet
from IEC61970.Base.Meas.AnalogLimit import AnalogLimit

class AnalogLimitSet(LimitSet):
    """An AnalogLimitSet specifies a set of Limits that are associated with an Analog
    measurement.
    """
    # The limit values used for supervision of Measurements.
    Limits= AnalogLimit()
