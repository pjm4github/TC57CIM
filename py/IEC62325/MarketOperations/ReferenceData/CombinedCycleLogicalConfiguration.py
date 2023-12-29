# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 13:18:10 2023
from typing import Any

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.ReferenceData.CombinedCycleConfiguration import CombinedCycleConfiguration
from IEC62325.MarketOperations.ReferenceData.MktCombinedCyclePlant import MktCombinedCyclePlant


class CombinedCycleLogicalConfiguration(IdentifiedObject):
    """
    Logical Configuration of a Combined Cycle plant.

    Operating Combined Cycle Plant (CCP) configurations are represented as Logical
    CCP Resources. Logical representation shall be used for Market applications to
    optimize and control Market Operations. Logical representation is also
    necessary for controlling the number of CCP configurations and to temper
    performance issues that may otherwise occur.

    For example,(2CT configuration),(1CT + 1ST configuration) are examples of
    logical configuration, without specifying the specific CT and ST participating
    in the configuration.
    @created 28-Dec-2023 1:03:01 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.mkt_combined_cycle_plant: Any = MktCombinedCyclePlant()
        self.combined_cycle_configuration: Any = CombinedCycleConfiguration()
