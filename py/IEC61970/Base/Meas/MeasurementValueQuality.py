###########################################################
# MeasurementValueQuality.py
# Implementation of the Class MeasurementValueQuality
# Created on:      18-Dec-2023 5:49:24 PM
###########################################################
from CIM_STD_PYTHON.TC57CIM.IEC61970.InfIEC61970.SCADA_EMS.Meas.MeasurementValueQualityExt import \
    MeasurementValueQualityExt
from Quality61850 import Quality61850


class MeasurementValueQuality(Quality61850, MeasurementValueQualityExt):
    def __init__(self):
        super().__init__()

