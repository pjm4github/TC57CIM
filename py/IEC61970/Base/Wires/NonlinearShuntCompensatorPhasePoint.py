# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Any

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Conductance import Conductance
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Susceptance import Susceptance


class NonlinearShuntCompensatorPhasePoint:
    """
    A per phase non linear shunt compensator bank or section admittance value.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """

        # Positive sequence shunt (charging) susceptance per section
        self.b: Susceptance = Susceptance()

        # Positive sequence shunt (charging) conductance per section
        self.g: Conductance = Conductance()

        # The number of the section.
        self.section_number: int = 0
    
    def get_b(self) -> Susceptance:
        return self.b

    def get_g(self) -> Conductance:
        return self.g

    def get_section_number(self) -> int:
        return self.section_number

    def set_b(self, new_val: Susceptance) -> None:
        self.b = new_val

    def set_g(self, new_val: Conductance) -> None:
        self.g = new_val

    def set_section_number(self, new_val: int) -> None:
        self.section_number = new_val
