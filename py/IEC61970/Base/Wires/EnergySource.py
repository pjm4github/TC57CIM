# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ActivePower import ActivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.AngleRadians import AngleRadians
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ReactivePower import ReactivePower
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.EnergyConnection import EnergyConnection




class EnergySource(EnergyConnection):
    """
    A generic equivalent for an energy supplier on a transmission or distribution
    voltage level.
    @author pmora
    @updated 15-Dec-2023 1:39:41 PM
    """
    def __init__(self):
        """
        Constructor for EnergySource class
        """
        super().__init__()
        self.active_power: ActivePower = ActivePower()  # High voltage source active injection.
        self.nominal_voltage: Voltage = Voltage()  # Phase-to-phase nominal voltage.
        self.r: Resistance = Resistance()  # Positive sequence Thevenin resistance.
        self.r0: Resistance = Resistance()  # Zero sequence Thevenin resistance.
        self.reactive_power: ReactivePower = ReactivePower()  # High voltage source reactive injection.
        self.rn: Resistance = Resistance()  # Negative sequence Thevenin resistance.
        self.voltage_angle: AngleRadians = AngleRadians()  # Phase angle of a-phase open circuit.
        self.voltage_magnitude: Voltage = Voltage()  # Phase-to-phase open circuit voltage magnitude.
        self.x: Reactance = Reactance()  # Positive sequence Thevenin reactance.
        self.x0: Reactance = Reactance()  # Zero sequence Thevenin reactance.
        self.xn: Reactance = Reactance()  # Negative sequence Thevenin reactance

    def get_active_power(self) -> Any:
        return self.active_power

    def get_nominal_voltage(self) -> Any:
        return self.nominal_voltage

    def get_r(self) -> Any:
        return self.r

    def get_r0(self) -> Any:
        return self.r0

    def get_reactive_power(self) -> Any:
        return self.reactive_power

    def get_rn(self) -> Any:
        return self.rn

    def get_voltage_angle(self) -> Any:
        return self.voltage_angle

    def get_voltage_magnitude(self) -> Any:
        return self.voltage_magnitude

    def get_x(self) -> Any:
        return self.x

    def get_x0(self) -> Any:
        return self.x0

    def get_xn(self) -> Any:
        return self.xn

    def set_active_power(self, new_val: Any) -> None:
        self.active_power = new_val

    def set_nominal_voltage(self, new_val: Any) -> None:
        self.nominal_voltage = new_val

    def set_r(self, new_val: Any) -> None:
        self.r = new_val

    def set_r0(self, new_val: Any) -> None:
        self.r0 = new_val

    def set_reactive_power(self, new_val: Any) -> None:
        self.reactive_power = new_val

    def set_rn(self, new_val: Any) -> None:
        self.rn = new_val

    def set_voltage_angle(self, new_val: Any) -> None:
        self.voltage_angle = new_val

    def set_voltage_magnitude(self, new_val: Any) -> None:
        self.voltage_magnitude = new_val

    def set_x(self, new_val: Any) -> None:
        self.x = new_val

    def set_x0(self, new_val: Any) -> None:
        self.x0 = new_val

    def set_xn(self, new_val: Any) -> None:
        self.xn = new_val
