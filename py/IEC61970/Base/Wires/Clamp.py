# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Length import Length


class Clamp:
    """
    A Clamp is a galvanic connection at a line segment where other equipment is
    connected. A Clamp does not cut the line segment.
    A Clamp is ConductingEquipment and has one Terminal with an associated
    ConnectivityNode. Any other ConductingEquipment can be connected to the Clamp
    ConnectivityNode.

    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self) -> None:
        self.length_from_terminal_1: Length = Length()

    def get_length_from_terminal_1(self) -> Length:
        return self.length_from_terminal_1

    def set_length_from_terminal_1(self, new_val: Length) -> None:
        self.length_from_terminal_1 = new_val
