#######################################################
# 
# MeasurementValueQualityExt.py
# Python implementation of the Class MeasurementValueQualityExt
# Generated by Enterprise Architect
# Created on:      18-Dec-2023 6:10:55 PM
# Original author: SELAOST1
# 
#######################################################
from IEC61970.InfIEC61970.SCADA_EMS.Meas.MeasurementConfigurationStatus import \
    MeasurementConfigurationStatus


class MeasurementValueQualityExt:

    def __init__(self):
        super().__init__()
        self.configuration_status = MeasurementConfigurationStatus.OK
