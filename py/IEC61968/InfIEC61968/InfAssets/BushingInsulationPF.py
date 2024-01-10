from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfAssets.BushingInsulationPfTestKind import BushingInsulationPfTestKind
from IEC61968.InfIEC61968.InfAssets.TransformerObservation import TransformerObservation
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject


class BushingInsulationPF(IdentifiedObject):
    def __init__(self):
        super().__init__()
        self.status = Status()
        self.test_kind = BushingInsulationPfTestKind.C1
        self.transformer_observation = TransformerObservation()
