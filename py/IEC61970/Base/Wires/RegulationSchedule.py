# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.RegulatingControl import RegulatingControl
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.VoltageControlZone import VoltageControlZone


class RegulationSchedule:
    """
    A pre-established pattern over time for a controlled variable, e.g., busbar
    voltage.
    @author pmora
    @updated 15-Dec-2023 1:39:42 PM
    """

    def __init__(self) -> None:
        self.regulating_control = RegulatingControl()
        self.voltage_control_zones = VoltageControlZone()

    def get_regulating_control(self) -> RegulatingControl:
        return self.regulating_control

    def get_voltage_control_zones(self) -> VoltageControlZone:
        return self.voltage_control_zones

    def set_regulating_control(self, new_val: RegulatingControl) -> None:
        self.regulating_control = new_val

    def set_voltage_control_zones(self, new_val: VoltageControlZone) -> None:
        self.voltage_control_zones = new_val
