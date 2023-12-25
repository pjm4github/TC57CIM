# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from typing import Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.SinglePhaseKind import SinglePhaseKind


class SwitchPhase:
    """
    Single phase of a multi-phase switch when its attributes might be different per
    phase.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:42 PM
    """

    def __init__(self) -> None:
        """
        The attribute tells if the switch is considered closed when used as input to
        topology processing.
        """
        self.closed: bool = False

        """
        Used in cases when no Measurement for the status value is present. If the
        SwitchPhase has a status measurement the Discrete.normalValue is expected to
        match with this value.
        """
        self.normal_open: bool = False

        """
        Phase of this SwitchPhase on the side with terminal sequence number equal 1.
        Should be a phase contained in that terminal's phases attribute.
        """
        self.phase_side1: Optional[SinglePhaseKind] = SinglePhaseKind.A

        """
        Phase of this SwitchPhase on the side with terminal sequence number equal 2.
        Should be a phase contained in that terminal's Terminal.phases attribute.
        """
        self.phase_side2: Optional[SinglePhaseKind] = SinglePhaseKind.B

    def get_closed(self) -> bool:
        return self.closed

    def get_normal_open(self) -> bool:
        return self.normal_open

    def get_phase_side1(self) -> Optional[SinglePhaseKind]:
        return self.phase_side1

    def get_phase_side2(self) -> Optional[SinglePhaseKind]:
        return self.phase_side2

    def set_closed(self, new_val: bool) -> None:
        self.closed = new_val

    def set_normal_open(self, new_val: bool) -> None:
        self.normal_open = new_val

    def set_phase_side1(self, new_val: SinglePhaseKind) -> None:
        self.phase_side1 = new_val

    def set_phase_side2(self, new_val: SinglePhaseKind) -> None:
        self.phase_side2 = new_val
