#######################################################
# 
# PinMeasurement.py
# Python implementation of the Class PinMeasurement
# Generated by Enterprise Architect
# Created on:      25-Dec-2023 8:32:01 PM
# Original author: sveinols
# 
#######################################################
from IEC61970.Base.Meas.Measurement import Measurement
from IEC61970.InfIEC61970.InfSIPS.GateInputPin import GateInputPin

class PinMeasurement(GateInputPin):
    """Gate input pin that is associated with a Measurement or a calculation of
    Measurement.
    """
    Measurement= Measurement()