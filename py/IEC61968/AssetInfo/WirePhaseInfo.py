# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetInfo.WireAssemblyInfo import WireAssemblyInfo
from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Wires.SinglePhaseKind import SinglePhaseKind
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.Structure import Structure
from CIM_STD_PYTHON.TC57CIM.IEC61968.Assets.DuctBank import DuctBank


class WirePhaseInfo:
    def __init__(self):
        self.phase_info = SinglePhaseKind.A
        self.wire_assembly_info = WireAssemblyInfo()
