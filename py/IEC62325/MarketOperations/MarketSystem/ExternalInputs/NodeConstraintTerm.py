# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from IEC62325.MarketOperations.MarketSystem.ConstraintTerm import ConstraintTerm  # Local import for Python
from IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode import MktConnectivityNode


class NodeConstraintTerm(ConstraintTerm):
    """
    To be used only to constrain a quantity that cannot be associated with a
    terminal. For example, a registered generating unit that is not electrically
    connected to the network.
    @created 27-Dec-2023 3:31:14 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.mkt_connectivity_node: MktConnectivityNode  = MktConnectivityNode()  # Assuming MktConnectivityNode is available in Python library
