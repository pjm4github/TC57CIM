# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetInfo.CableInfo import CableInfo
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.Length import Length
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.PerCent import PerCent


class TapeShieldCableInfo(CableInfo):

    def __init__(self):
        super().__init__()
        self.tape_lap = PerCent()
        self.tape_thickness = Length()
