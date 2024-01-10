# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 12:50:20 2023
from typing import Optional

from IEC62325.MarketOperations.MarketSystem.ExternalInputs.Profile import Profile
from IEC62325.InfIEC62325.InfFinancial.TransmissionProvider import TransmissionProvider

class LossProfile(Profile):
    """
    LossProfile is associated with an EnergyTransaction and must be completely
    contained within the time frame of the EnergyProfile associated with this
    EnergyTransaction.
    @created 27-Dec-2023 12:44:44 PM
    """

    # Part of the LossProfile for an EnergyTransaction may be a loss for a
    # TransmissionProvider. If so, the TransmissionProvider must be one of the
    # participating entities in the EnergyTransaction.

    def __init__(self) -> None:
        super().__init__()
        self.has_loss: Optional[TransmissionProvider] = TransmissionProvider()
