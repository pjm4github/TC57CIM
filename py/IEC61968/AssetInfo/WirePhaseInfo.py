# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from IEC61968.AssetInfo.WireAssemblyInfo import WireAssemblyInfo
from IEC61970.Base.Wires.SinglePhaseKind import SinglePhaseKind
from IEC61968.Assets.Structure import Structure
from IEC61968.Assets.DuctBank import DuctBank


class WirePhaseInfo:
    def __init__(self):
        self.phase_info = SinglePhaseKind.A
        self.wire_assembly_info = WireAssemblyInfo()
