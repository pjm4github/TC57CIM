# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode import MktConnectivityNode
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.GenDistributionFactor import GenDistributionFactor
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.LoadDistributionFactor import LoadDistributionFactor
from IEC62325.MarketOperations.ReferenceData.Pnode import Pnode
from IEC62325.MarketOperations.ReferenceData.PnodeDistributionFactor import PnodeDistributionFactor


class IndividualPnode(Pnode):
    def __init__(self) -> None:
        super().__init__()
        self.pnode_distribution_factor: PnodeDistributionFactor = PnodeDistributionFactor()
        self.gen_distribution_factor: GenDistributionFactor = GenDistributionFactor()
        self.load_distribution_factor: LoadDistributionFactor = LoadDistributionFactor()
        self.mkt_connectivity_node: MktConnectivityNode = MktConnectivityNode()
