# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from typing import Optional

from IEC61968.Assets.AssetInfo import AssetInfo
from IEC61968.InfIEC61968.InfCommon.Ratio import Ratio
from IEC61970.Base.Domain.Voltage import Voltage


class PotentialTransformerInfo(AssetInfo):

    def __init__(self) -> None:
        super().__init__()
        self.accuracy_classOptional[str] = ""
        self.nominal_ratioOptional[Ratio] = Ratio()
        self.primary_ratioOptional[Ratio] = Ratio()
        self.pt_classOptional[str] = ""
        self.rated_voltageOptional[Voltage] = Voltage()
        self.secondary_ratioOptional[Ratio] = Ratio()
        self.tertiary_ratioOptional[Ratio] = Ratio()
