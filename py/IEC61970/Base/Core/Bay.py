#######################################################
# 
# Bay.py
# Python implementation of the Class Bay
# Generated by Enterprise Architect
# Created on:      16-Dec-2023 4:56:39 PM
# 
#######################################################

from IEC61970.Base.Core.BreakerConfiguration import BreakerConfiguration
from IEC61970.Base.Core.BusbarConfiguration import BusbarConfiguration
from IEC61970.Base.Core.EquipmentContainer import EquipmentContainer


class Bay(EquipmentContainer):
    """A collection of power system resources (within a given substation) including
    conducting equipment, protection relays, measurements, and telemetry.  A bay
    typically represents a physical grouping related to modularization of equipment.
    """

    def __init__(self):
        super().__init__()
        self.bay_energy_meas_flag: bool = False
        self.bay_power_meas_flag: bool = False
        self.breaker_configuration: BreakerConfiguration = BreakerConfiguration.SINGLE_BREAKER
        self.bus_bar_configuration: BusbarConfiguration = BusbarConfiguration.SINGLE_BUS
