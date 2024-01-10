# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 13:18:10 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.ReferenceData.MktThermalGeneratingUnit import MktThermalGeneratingUnit


class CombinedCycleConfigurationMember(IdentifiedObject):
    """
    Configuration Member of CCP Configuration.
    @updated 28-Dec-2023 1:02:50 PM
    """

    def __init__(self) -> None:
        """
        Construct CombinedCycleConfigurationMember
        """
        super().__init__()
        self.primary: bool = False  # primary configuration
        self.steam: bool = False  # Steam plant
        self.mkt_thermal_generating_unit: Optional[MktThermalGeneratingUnit] = MktThermalGeneratingUnit()
