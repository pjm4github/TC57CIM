# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 13:18:10 2023
from typing import Optional

from IEC62325.MarketOperations.ReferenceData.CombinedCycleConfigurationMember import CombinedCycleConfigurationMember
from IEC62325.MarketOperations.ReferenceData.CombinedCycleTransitionState import CombinedCycleTransitionState
from IEC62325.MarketOperations.ReferenceData.RegisteredGenerator import RegisteredGenerator


class CombinedCycleConfiguration(RegisteredGenerator):
    """
    Configuration options for combined cycle units.

    For example, a Combined Cycle with (CT1, CT2, ST1) will have (CT1, ST1) and
    (CT2, ST1) configurations as part of(1CT + 1STlogicalconfiguration).
    @created 28-Dec-2023 1:02:18 PM
    """
    def __init__(self) -> None:
        """Initialize CombinedCycleConfiguration attributes."""
        # Whether this CombinedCycleConfiguration is the primary configuration in the
        # associated Logical configuration?
        super().__init__()
        self.primary_configurationbool = False
        # Whether Combined Cycle Plant can be shut-down in this Configuration?
        self.shutdown_flagbool = False
        # Whether Combined Cycle Plant can be started in this Logical Configuration?
        self.startup_flagbool = False
        self.to_transition_stateOptional[CombinedCycleTransitionState] = CombinedCycleTransitionState()
        self.from_transition_stateOptional[CombinedCycleTransitionState] = CombinedCycleTransitionState()
        self.combined_cycle_configuration_memberOptional[CombinedCycleConfigurationMember] =\
            CombinedCycleConfigurationMember()

