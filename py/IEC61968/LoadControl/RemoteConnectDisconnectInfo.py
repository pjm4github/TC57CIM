#######################################################
# 
# RemoteConnectDisconnectInfo.py
# Python implementation of the Class RemoteConnectDisconnectInfo
# Generated by Enterprise Architect
# Created on:      19-Dec-2023 9:20:50 PM
# Original author: T. Kostic
# 
#######################################################
from IEC61970.Base.Domain.ActivePower import ActivePower
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.RealEnergy import RealEnergy
from IEC61970.Base.Domain.Seconds import Seconds
from IEC61970.Base.Domain.Voltage import Voltage


class RemoteConnectDisconnectInfo:
    """
    Details of remote connect and disconnect function.
    """
    def __init__(self):
        self.armed_timeout = Seconds()
        self.customer_voltage_limit = Voltage()
        self.energy_limit = RealEnergy()
        self.energy_usage_start_date_time = DateTime()
        self.energy_usage_warning = RealEnergy()
        self.is_arm_connect = False
        self.is_arm_disconnect = False
        self.is_energy_limiting = False
        self.needs_power_limit_check = False
        self.needs_voltage_limit_check = False
        self.power_limit = ActivePower()
        self.use_pushbutton = False
