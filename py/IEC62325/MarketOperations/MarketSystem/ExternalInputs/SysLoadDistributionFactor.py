# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode import MktConnectivityNode

class SysLoadDistributionFactor:
    """
    This class models the system distribution factors. This class needs to be used
    along with the HostControlArea and the ConnectivityNode to show the
    distribution of each individual party.
    @created 27-Dec-2023 3:32:34 PM
    """

    def __init__(self) -> None:
        """
        Used to calculate load "participation" of a connectivity node in an 
        host control area
        """
        self.factor: float
        self.mkt_connectivity_node: MktConnectivityNode = MktConnectivityNode()
