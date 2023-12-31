#######################################################
# 
# CurrentTransformer.py
# Python implementation of the Class CurrentTransformer
# Generated by Enterprise Architect
# Created on:      18-Dec-2023 8:53:00 PM
# 
#######################################################
# from IEC61970.Base.Domain.String import String
from IEC61970.Base.Domain.PerCent import PerCent
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.AuxiliaryEquipment.Sensor import Sensor

class CurrentTransformer(Sensor):
    """Instrument transformer used to measure electrical qualities of the circuit that
    is being protected and/or monitored. Typically used as current transducer for
    the purpose of metering or protection. A typical secondary current rating would
    be 5A.
    """

    def __init__(self):
        super().__init__()
        self.accuracy_class = ""
        self.accuracy_limit = PerCent()  # Percent of rated current for which the CT remains accurate within specified limits.
        self.core_burden = ActivePower()  # Power burden of the CT core.
        self.ct_class = ""  # CT classification; i.e. class 10P.
        self.usage = ""  # Intended usage of the CT; i.e. metering, protection.
