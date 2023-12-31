#######################################################
# 
# AnalogLimitSet.py
# Python implementation of the Class AnalogLimitSet
# Generated by Enterprise Architect
# Created on:      20-Dec-2023 11:07:17 AM
# 
#######################################################

class AnalogLimitSet(LimitSet):
    """An AnalogLimitSet specifies a set of Limits that are associated with an Analog
    measurement.
    """
    def __init__(self):
        self.limits = AnalogLimit()    # The limit values used for supervision of Measurements.
