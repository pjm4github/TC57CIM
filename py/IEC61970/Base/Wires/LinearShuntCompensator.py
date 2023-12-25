# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Susceptance import Susceptance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.NonlinearShuntCompensatorPhasePoint import Conductance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ShuntCompensator import ShuntCompensator


class LinearShuntCompensator(ShuntCompensator):

    def __init__(self) -> None:
        super().__init__()
        self.b0_per_section: Susceptance = Susceptance()  # Zero sequence shunt (charging) susceptance per section
        self.b_per_section: Susceptance = Susceptance()  # Positive sequence shunt (charging) susceptance per section
        self.g0_per_section: Conductance = Conductance()  # Zero sequence shunt (charging) conductance per section
        self.g_per_section: Conductance = Conductance()  # Positive sequence shunt (charging) conductance per section

    def get_b0_per_section(self) -> Any:
        return self.b0_per_section

    def get_b_per_section(self) -> Any:
        return self.b_per_section

    def get_g0_per_section(self) -> Any:
        return self.g0_per_section

    def get_g_per_section(self) -> Any:
        return self.g_per_section

    def set_b0_per_section(self, new_val: Any) -> None:
        self.b0_per_section = new_val

    def set_b_per_section(self, new_val: Any) -> None:
        self.b_per_section = new_val

    def set_g0_per_section(self, new_val: Any) -> None:
        self.g0_per_section = new_val

    def set_g_per_section(self, new_val: Any) -> None:
        self.g_per_section = new_val
