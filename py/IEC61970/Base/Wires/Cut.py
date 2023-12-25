# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Length import Length
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ACLineSegment import ACLineSegment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.Switch import Switch


class Cut(Switch):
    def __init__(self) -> None:
        super().__init__()
        self.ac_line_segment = ACLineSegment()
        self.length_from_terminal1 = Length()

    def get_ac_line_segment(self) -> ACLineSegment:
        return self.ac_line_segment

    def get_length_from_terminal1(self) -> Length:
        return self.length_from_terminal1

    def set_ac_line_segment(self, new_val: ACLineSegment) -> None:
        self.ac_line_segment = new_val

    def set_length_from_terminal1(self, new_val: Length) -> None:
        self.length_from_terminal1 = new_val
