# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 16:45:14 2023

from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Resistance import Resistance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Voltage import Voltage


class SeriesCompensator:
    """
    A Series Compensator is a series capacitor or reactor or an AC transmission
    line without charging susceptance. It is a two terminal device.
    @author pmora
    @created 15-Dec-2023 4:38:29 PM
    """
    def __init__(self) -> None:
        """
        Constructor
        """
        self.r: Optional[Resistance] = Resistance()  # Positive sequence resistance.
        self.r0: Optional[Resistance] = Resistance()  # Zero sequence resistance.
        self.varistor_present: bool = False  # Describe if a metal oxide varistor (mov) for overvoltage protection is
        # configured at the series compensator.
        self.varistor_rated_current: Optional[CurrentFlow] = CurrentFlow()  # The maximum current the varistor is designed to handle
        # at specified duration.
        self.varistor_voltage_threshold: Optional[Voltage] = Voltage()  # The dc voltage at which the varistor start conducting.
        self.x: Optional[Reactance] = Reactance()  # Positive sequence reactance.
        self.x0: Optional[Reactance] = Reactance()  # Zero sequence reactance.

    def get_r(self) -> Resistance:
        return self.r

    def get_r0(self) -> Resistance:
        return self.r0

    def get_varistor_present(self) -> bool:
        return self.varistor_present

    def get_varistor_rated_current(self) -> CurrentFlow:
        return self.varistor_rated_current

    def get_varistor_voltage_threshold(self) -> Voltage:
        return self.varistor_voltage_threshold

    def get_x(self) -> Reactance:
        return self.x

    def get_x0(self) -> Reactance:
        return self.x0

    def set_r(self, new_val: Resistance) -> None:
        self.r = new_val

    def set_r0(self, new_val: Resistance) -> None:
        self.r0 = new_val

    def set_varistor_present(self, new_val: bool) -> None:
        self.varistor_present = new_val

    def set_varistor_rated_current(self, new_val: CurrentFlow) -> None:
        self.varistor_rated_current = new_val

    def set_varistor_voltage_threshold(self, new_val: Voltage) -> None:
        self.varistor_voltage_threshold = new_val

    def set_x(self, new_val: Reactance) -> None:
        self.x = new_val

    def set_x0(self, new_val: Reactance) -> None:
        self.x0 = new_val
