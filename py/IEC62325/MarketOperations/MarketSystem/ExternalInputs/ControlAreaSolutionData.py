# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from typing import Optional

from IEC62325.MarketOperations.MarketSystem.ExternalInputs.MktControlArea import MktControlArea


class ControlAreaSolutionData:
    """
    State Estimator Solution Pool Interchange and Losses.
    """
    def __init__(self) -> None:
        """
        Constructor for ControlAreaSolutionData
        """
        # 	 * Pool MW Interchange
        # 	 * Attribute Usage: The active power interchange of the pool
        self.solved_interchange: Optional[float] = 0.0
        # 	 * Pool Losses MW
        # 	 * Attribute Usage: The active power losses of the pool in MW
        self.solved_losses: Optional[float] = 0.0
        self.mkt_control_area: Optional[MktControlArea] = MktControlArea()
