from IEC61968.Assets.Asset import Asset
from IEC61968.InfIEC61968.InfAssets.BushingInsulationPF import BushingInsulationPF
from IEC61970.Base.Core.Terminal import Terminal


class Bushing(Asset):
    def __init__(self):
        super().__init__()
        self.bushing_insulation_pfs = BushingInsulationPF()
        self.terminal = Terminal()
