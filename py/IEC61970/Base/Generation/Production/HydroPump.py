#######################################################
# 
# HydroPump.py
# Python implementation of the Class HydroPump
# Generated by Enterprise Architect
# Created on:      18-Dec-2023 1:19:17 PM
# 
#######################################################
from IEC61970.Base.Domain.VolumeFlowRate import VolumeFlowRate
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Core.Equipment import Equipment
from IEC61970.Base.Generation.Production.HydroPumpOpSchedule import HydroPumpOpSchedule

class HydroPump(Equipment):
    """A synchronous motor-driven pump, typically associated with a pumped storage
    plant.
    """
    def __init__(self):
        super().__init__()
        # The pumping discharge under maximum head conditions, usually at full gate.
        self.pump_disch_at_max_head = VolumeFlowRate()
        # The pumping discharge under minimum head conditions, usually at full gate.
        self.pump_disch_at_min_head = VolumeFlowRate()
        # The pumping power under maximum head conditions, usually at full gate.
        self.pump_power_at_max_head = ActivePower()
        # The pumping power under minimum head conditions, usually at full gate.
        self.pump_power_at_min_head = ActivePower()
        # The hydro pump has a pumping schedule over time, indicating when pumping is to occur.
        self.hydro_pump_op_schedule = HydroPumpOpSchedule()
