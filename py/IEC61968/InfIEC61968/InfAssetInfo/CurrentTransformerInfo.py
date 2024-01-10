# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from typing import Optional

from IEC61968.Assets.AssetInfo import AssetInfo
from IEC61968.InfIEC61968.InfCommon.Ratio import Ratio
from IEC61970.Base.Domain.CurrentFlow import CurrentFlow
from IEC61970.Base.Domain.Voltage import Voltage


class CurrentTransformerInfo(AssetInfo):
    """
    Properties of current transformer asset.
    @created 29-Dec-2023 6:22:08 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.accuracy_class: Optional[str] = ""  # CT accuracy classification
        self.accuracy_limit: Optional[CurrentFlow] = CurrentFlow()  # Accuracy limit
        self.core_count: Optional[int] = 0  # Number of cores
        self.ct_class: Optional[str] = ""
        self.knee_point_current: Optional[CurrentFlow] = CurrentFlow()  # Maximum primary current where the CT still displays linear characteristics
        self.knee_point_voltage: Optional[Voltage] = Voltage()  # Maximum voltage across the secondary terminals where the CT still displays linear characteristics
        self.max_ratio: Optional[Ratio] = Ratio()  # Maximum ratio between the primary and secondary current
        self.nominal_ratio: Optional[Ratio] = Ratio()  # Nominal ratio between the primary and secondary current; i.e. 100:5
        self.primary_fls_rating: Optional[CurrentFlow] = CurrentFlow()  # Full load secondary (FLS) rating for primary winding
        self.primary_ratio: Optional[Ratio] = Ratio()  # Ratio for the primary winding tap changer
        self.rated_current: Optional[CurrentFlow] = CurrentFlow()  # Rated current on the primary side
        self.secondary_fls_rating: Optional[CurrentFlow] = CurrentFlow()  # Full load secondary (FLS) rating for secondary winding
        self.secondary_ratio: Optional[Ratio] = Ratio()  # Ratio for the secondary winding tap changer
        self.tertiary_fls_rating: Optional[CurrentFlow] = CurrentFlow()  # Full load secondary (FLS) rating for tertiary winding
        self.tertiary_ratio: Optional[Ratio] = Ratio()  # Ratio for the tertiary winding tap changer
        self.usage: Optional[str] = ""  # Usage: e.g. metering, protection, etc.
