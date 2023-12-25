# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:35:24 2023
# local import assuming type Length and ACLineSegment are available as Python library
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Length import Length
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Faults import Fault
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ACLineSegment import ACLineSegment


class LineFault(Fault):
    """
    A fault that occurs on an AC line segment at some point along the length.
    @author kdemaree
    @version 1.0
    @created 15-Dec-2023 4:38:28 PM
    """
    def __init__(self) -> None:
        """
        The length to the place where the fault is located starting from terminal with
        sequence number 1 of the faulted line segment.
        """
        self.length_from_terminal_1: Length = Length()

        """
        The line segment of this line fault.
        """
        self.ac_line_segment: ACLineSegment = ACLineSegment()
