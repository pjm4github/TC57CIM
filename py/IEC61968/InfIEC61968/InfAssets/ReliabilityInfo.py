# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from IEC61968.Assets.Asset import Asset
from IEC61968.InfIEC61968.InfAssets.Specification import Specification
from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.Hours import Hours
from IEC61970.Base.Domain.PerCent import PerCent


class ReliabilityInfo(IdentifiedObject):
    """
    Information regarding the experienced and expected reliability of a specific
    asset, type of asset, or asset model.
    @created 29-Dec-2023 6:12:04 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.mom_failure_rate = PerCent()  # Momentary failure rate (temporary failures/kft-year).
        self.mttr = Hours()  # Mean-time-to-repair (MTTR - hours).
        self.specification = Specification()
        self.assets = Asset()
