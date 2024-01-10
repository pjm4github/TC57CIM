# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors
from IEC62325.MarketOperations.MarketSystem.MarketResults.Commitments import Commitments


class CommitmentClearing(MarketFactors):
    """
    Models results of market clearing which call for commitment of units.
    @created 28-Dec-2023 8:19:00 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.commitments = Commitments()
