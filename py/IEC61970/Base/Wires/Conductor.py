# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Length import Length


class Conductor:
    """
    Combination of conducting material with consistent electrical characteristics,
    building a single electrical system, used to carry current between points in
    the power system.
    @author pmora
    @updated 15-Dec-2023 1:39:41 PM
    """

    def __init__(self) -> None:
        self.length: Length = Length() # Segment length for calculating line section capabilities

    def get_length(self) -> Length:
        return self.length

    def set_length(self, new_val: Length) -> None:
        self.length = new_val
