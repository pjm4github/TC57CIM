# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors

from IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode import MktConnectivityNode


class LossSensitivity(MarketFactors):
    """
    Loss sensitivity applied to a ConnectivityNode for a given time interval.
    @created 27-Dec-2023 3:30:24 PM
    """

    def __init__(self) -> None:
        """
        Loss penalty factor.
        Defined as: 1 / (1 - Incremental Transmission Loss);
        with the Incremental Transmission Loss expressed as a plus or minus value.
        The typical range of penalty factors is (0.9 to 1.1).
        """
        super().__init__()
        self.loss_factor: float = 0.0
        self.mkt_connectivity_node: MktConnectivityNode = MktConnectivityNode()
