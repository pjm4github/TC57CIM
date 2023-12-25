# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.ACLineSegment import ACLineSegment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PerLengthLineParameter import PerLengthLineParameter


class PerLengthImpedance(PerLengthLineParameter):

    '''
    Common type for per-length impedance electrical catalogues.
    @author pmora
    @version 1.0
    @updated 15-Dec-2023 1:39:41 PM
    '''

    '''
    All line segments described by this per-length impedance.
    '''
    def __init__(self):
        super().__init__()
        self._ac_line_segments = ACLineSegment()

    def get_ac_line_segments(self) -> ACLineSegment:
        return self._ac_line_segments

    '''
    @param newVal
    '''
    def set_ac_line_segments(self, new_val: ACLineSegment) -> None:
        self._ac_line_segments = new_val
