# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.SinglePhaseKind import SinglePhaseKind


class ShuntCompensatorPhase:

    def __init__(self) -> None:
        self.maximum_sections: Optional[
            int] = 0  # The maximum number of sections that may be switched in for this phase
        self.normal_sections: Optional[
            int] = 0  # For the capacitor phase, the normal number of sections switched in
        self.phase: Optional[SinglePhaseKind] = SinglePhaseKind.A  # Phase of this shunt compensator component

    def get_maximum_sections(self) -> Optional[int]:
        return self.maximum_sections

    def get_normal_sections(self) -> Optional[int]:
        return self.normal_sections

    def get_phase(self) -> Optional[SinglePhaseKind]:
        return self.phase

    def set_maximum_sections(self, new_val: int) -> None:
        self.maximum_sections = new_val

    def set_normal_sections(self, new_val: int) -> None:
        self.normal_sections = new_val

    def set_phase(self, new_val: SinglePhaseKind) -> None:
        self.phase = new_val
