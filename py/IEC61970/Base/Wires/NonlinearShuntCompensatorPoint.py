# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Conductance import Conductance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Susceptance import Susceptance


class NonlinearShuntCompensatorPoint:
    """
    A non linear shunt compensator bank or section admittance value.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """

        # Positive sequence shunt (charging) susceptance per section
        self.b: Optional[Susceptance] = Susceptance()

        # Zero sequence shunt (charging) susceptance per section
        self.b0: Optional[Susceptance] = Susceptance()

        # Positive sequence shunt (charging) conductance per section
        self.g: Optional[Conductance] = Conductance()

        # Zero sequence shunt (charging) conductance per section
        self.g0: Optional[Conductance] = Conductance()

        # The number of the section
        self.section_number: int = 0

    def get_b(self) -> Optional[Susceptance]:
        return self.b

    def get_b0(self) -> Optional[Susceptance]:
        return self.b0

    def get_g(self) -> Optional[Conductance]:
        return self.g

    def get_g0(self) -> Optional[Conductance]:
        return self.g0

    def get_section_number(self) -> int:
        return self.section_number

    def set_b(self, new_val: Susceptance) -> None:
        self.b = new_val

    def set_b0(self, new_val: Susceptance) -> None:
        self.b0 = new_val

    def set_g(self, new_val: Conductance) -> None:
        self.g = new_val

    def set_g0(self, new_val: Conductance) -> None:
        self.g0 = new_val

    def set_section_number(self, new_val: int) -> None:
        self.section_number = new_val


