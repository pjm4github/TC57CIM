# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors


class ExPostPricing(MarketFactors):
    """
    Model of ex-post pricing of nodes.
    @created 28-Dec-2023 8:20:46 PM
    """

    def __init__(self) -> None:
        """
        Constructor for ExPostPricing class.
        """
        super().__init__()
        self.energy_price: float = 0.0
