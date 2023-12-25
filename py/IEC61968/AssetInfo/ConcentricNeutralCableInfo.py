# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Length import Length
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.ResistancePerLength import ResistancePerLength

class ConcentricNeutralCableInfo:
    
    def __init__(self):
        self.diameter_over_neutral = Length()
        self.neutral_strand_count = 0
        self.neutral_strand_gmr = Length()
        self.neutral_strand_radius = Length()
        self.neutral_strand_rdc20 = ResistancePerLength()
