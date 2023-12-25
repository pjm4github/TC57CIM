# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.CapacitancePerLength import CapacitancePerLength
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.InductancePerLength import InductancePerLength
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ResistancePerLength import ResistancePerLength
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.DC.DCLineSegment import DCLineSegment
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class PerLengthDCLineParameter(IdentifiedObject):
    def __init__(self) -> None:
        super().__init__()
        self.capacitance: CapacitancePerLength = CapacitancePerLength()
        self.inductance: InductancePerLength = InductancePerLength()
        self.resistance: ResistancePerLength = ResistancePerLength()
        self.dc_line_segments: DCLineSegment = DCLineSegment()

