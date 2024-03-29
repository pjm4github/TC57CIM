#######################################################
# 
# RemoteUnit.py
# Python implementation of the Class RemoteUnit
# Generated by Enterprise Architect
# Created on:      17-Dec-2023 7:19:13 PM
# 
#######################################################
from IEC61970.Base.SCADA.RemoteUnitType import RemoteUnitType
from IEC61970.Base.Core.PowerSystemResource import PowerSystemResource
from IEC61970.Base.SCADA.RemotePoint import RemotePoint

class RemoteUnit(PowerSystemResource):
    """A remote unit can be a RTU, IED, substation control system, control center etc.
    The communication with the remote unit can be through various standard
    protocols (e.g. IEC 61870, IEC 61850) or non standard protocols (e.g. DNP,
    RP570 etc.). A remote unit contain remote data points that might be telemetered,
    collected or calculated. The RemoteUnit class inherit PowerSystemResource. The
    intention is to allow RemotUnits to have Measurements. These Measurements can
    be used to model unit status as operational, out of service, unit failure etc.
    """

    def __init__(self):
        super().__init__()
        self.remote_points = [RemotePoint()]  # Remote points this Remote unit contains.
        self.remote_unit_type = RemoteUnitType.IED