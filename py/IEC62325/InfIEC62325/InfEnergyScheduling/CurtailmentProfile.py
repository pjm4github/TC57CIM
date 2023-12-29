# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 12:50:20 2023
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.Profile import Profile


class CurtailmentProfile(Profile):
    """
    Curtailing entity must be providing at least one service to the
    EnergyTransaction. The CurtailmentProfile must be completely contained within
    the EnergyProfile timeframe for this EnergyTransaction.
    @created 27-Dec-2023 12:43:50 PM
    """
    def __init__(self) -> None:
        super().__init__()
