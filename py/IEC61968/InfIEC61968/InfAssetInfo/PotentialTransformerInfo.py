# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from typing import Optional

from IEC61968.Assets.AssetInfo import AssetInfo
from IEC61968.InfIEC61968.InfCommon.Ratio import Ratio
from IEC61970.Base.Domain.Voltage import Voltage


class PotentialTransformerInfo(AssetInfo):

    def __init__(self) -> None:
        super().__init__()
        self.accuracy_class: Optional[str] = ""
        self.nominal_ratio: Optional[Ratio] = Ratio()
        self.primary_ratio: Optional[Ratio] = Ratio()
        self.pt_class: Optional[str] = ""
        self.rated_voltage: Optional[Voltage] = Voltage()
        self.secondary_ratio: Optional[Ratio] = Ratio()
        self.tertiary_ratio: Optional[Ratio] = Ratio()
