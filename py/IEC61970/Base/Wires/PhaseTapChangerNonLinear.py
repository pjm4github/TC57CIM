# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Any, Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PerCent import PerCent
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Reactance import Reactance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PhaseTapChanger import PhaseTapChanger


class PhaseTapChangerNonLinear(PhaseTapChanger):
    """
    The non-linear phase tap changer describes the non-linear behavior of a phase
    tap changer. This is a base class for the symmetrical and asymmetrical phase
    tap changer models. The details of these models can be found in the IEC 61970-
    301 document.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.voltage_step_increment: Optional[PerCent] = PerCent()  # The voltage step increment on the out of phase winding specified in percent of neutral voltage of the tap changer.
        self.x_max: Optional[Reactance] = Reactance()  # The reactance depend on the tap position according to a "u" shaped curve. The maximum reactance (xMax) appear at the low and high tap positions.
        self.x_min: Optional[Reactance] = Reactance()  # The reactance depend on the tap position according to a "u" shaped curve. The minimum reactance (xMin) appear at the mid tap position.

    def get_voltage_step_increment(self) -> Optional[PerCent]:
        return self.voltage_step_increment

    def get_x_max(self) -> Optional[Reactance]:
        return self.x_max

    def get_x_min(self) -> Optional[Reactance]:
        return self.x_min

    def set_voltage_step_increment(self, new_val: PerCent) -> None:
        self.voltage_step_increment = new_val

    def set_x_max(self, new_val: Reactance) -> None:
        self.x_max = new_val

    def set_x_min(self, new_val: Reactance) -> None:
        self.x_min = new_val
