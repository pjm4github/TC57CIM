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
        self.accuracy_classOptional[str] = ""  # CT accuracy classification
        self.accuracy_limitOptional[CurrentFlow] = CurrentFlow()  # Accuracy limit
        self.core_countOptional[int] = 0  # Number of cores
        self.ct_classOptional[str] = ""
        self.knee_point_currentOptional[CurrentFlow] = CurrentFlow()  # Maximum primary current where the CT still displays linear characteristics
        self.knee_point_voltageOptional[Voltage] = Voltage()  # Maximum voltage across the secondary terminals where the CT still displays linear characteristics
        self.max_ratioOptional[Ratio] = Ratio()  # Maximum ratio between the primary and secondary current
        self.nominal_ratioOptional[Ratio] = Ratio()  # Nominal ratio between the primary and secondary current; i.e. 100:5
        self.primary_fls_ratingOptional[CurrentFlow] =  CurrentFlow()  # Full load secondary (FLS) rating for primary winding
        self.primary_ratioOptional[Ratio] = Ratio()  # Ratio for the primary winding tap changer
        self.rated_currentOptional[CurrentFlow] = CurrentFlow()  # Rated current on the primary side
        self.secondary_fls_ratingOptional[CurrentFlow] = CurrentFlow()  # Full load secondary (FLS) rating for secondary winding
        self.secondary_ratioOptional[Ratio] = Ratio()  # Ratio for the secondary winding tap changer
        self.tertiary_fls_ratingOptional[CurrentFlow] =  CurrentFlow()  # Full load secondary (FLS) rating for tertiary winding
        self.tertiary_ratioOptional[Ratio] = Ratio()  # Ratio for the tertiary winding tap changer
        self.usageOptional[str] = ""  # Usage: e.g. metering, protection, etc.
