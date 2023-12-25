# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.Connector import Connector
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.VoltageControlZone import VoltageControlZone


class BusbarSection(Connector):
    """
    A conductor, or group of conductors, with negligible impedance, that serve to
    connect other conducting equipment within a single substation.
    Voltage measurements are typically obtained from VoltageTransformers that are
    connected to busbar sections. A bus bar section may have many physical
    terminals but for analysis is modelled with exactly one logical terminal.
    @author pmora
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.ip_max: Optional[CurrentFlow] = CurrentFlow()
        self.voltage_control_zone: Optional[VoltageControlZone] = None

    def get_ip_max(self) -> CurrentFlow:
        return self.ip_max

    def get_voltage_control_zone(self) -> VoltageControlZone:
        return self.voltage_control_zone

    def set_ip_max(self, new_val: CurrentFlow) -> None:
        self.ip_max = new_val

    def set_voltage_control_zone(self, new_val: VoltageControlZone) -> None:
        self.voltage_control_zone = new_val
