# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 13:18:10 2023
from typing import Optional

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode import MktConnectivityNode
from IEC62325.MarketOperations.ReferenceData.SubControlArea import SubControlArea


class CnodeDistributionFactor(IdentifiedObject):
    """
    Participation factors per Cnode. Used to calculate "participation" of Cnode in
    an AggregateNode. Each Cnode associated to an AggregateNode would be assigned a
    participation factor for its participation within the AggregateNode.
    @created 28-Dec-2023 1:02:08 PM
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of CnodeDistributionFactor.
        """
        super().__init__()
        self.factor: float = 0.0  # Used to calculate "participation" of Cnode in an AggregateNode
        self.pod_loss_factor: float = 0.0  # Point of delivery loss factor
        self.sub_control_area: Optional[SubControlArea] = SubControlArea()
        self.mkt_connectivity_node: Optional[MktConnectivityNode] = MktConnectivityNode()
