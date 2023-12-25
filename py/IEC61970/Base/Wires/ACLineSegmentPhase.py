from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.StateVariables.SvVoltage import SinglePhaseKind
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ACLineSegment import ACLineSegment


class ACLineSegmentPhase:
    def __init__(self):
        self.phase: SinglePhaseKind = SinglePhaseKind.A # The phase connection of the wire at both ends
        self.sequence_number = 0  # Number designation for this line segment phase
        self.ac_line_segment = ACLineSegment()  # The line segment to which the phase belongs

    def get_ac_line_segment(self) -> ACLineSegment:
        return self.ac_line_segment

    def get_phase(self) -> SinglePhaseKind:
        return self.phase

    def get_sequence_number(self) -> int:
        return self.sequence_number

    def set_ac_line_segment(self, new_val: ACLineSegment):
        self.ac_line_segment = new_val

    def set_phase(self, new_val: SinglePhaseKind):
        self.phase = new_val

    def set_sequence_number(self, new_val: int):
        self.sequence_number = new_val
