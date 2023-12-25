# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106


from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.AssetInfo import AssetInfo
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.PerLengthLineParameter import PerLengthLineParameter


class WireAssemblyInfo(AssetInfo):

    def __init__(self):
        super().__init__()
        self.per_length_line_parameter = PerLengthLineParameter()
