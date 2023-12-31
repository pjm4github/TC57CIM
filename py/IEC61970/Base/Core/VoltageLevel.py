#######################################################
# 
# VoltageLevel.py
# Python implementation of the Class VoltageLevel
# Generated by Enterprise Architect
# Created on:      16-Dec-2023 6:34:02 PM
# 
#######################################################
from IEC61970.Base.Domain.Voltage import Voltage
from IEC61970.Base.Core.EquipmentContainer import EquipmentContainer
from IEC61970.Base.Core.Bay import Bay
from IEC61970.Base.Core.BaseVoltage import BaseVoltage

class VoltageLevel(EquipmentContainer):
    """A collection of equipment at one common system voltage forming a switchgear.
    The equipment typically consist of breakers, busbars, instrumentation, control,
    regulation and protection devices as well as assemblies of all these.
    """
    def __init__(self):
        super().__init__()
        self.high_voltage_limit = Voltage()  # The bus bar's high voltage limit
        self.low_voltage_limit = Voltage()  # The bus bar's low voltage limit
        self.bays = Bay()  # The bays within this voltage level.
        self.base_voltage = BaseVoltage()  # The base voltage used for all equipment within the voltage level.
