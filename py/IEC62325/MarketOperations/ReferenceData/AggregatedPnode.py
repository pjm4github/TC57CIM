# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 13:18:10 2023
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.GenDistributionFactor import GenDistributionFactor
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.LoadDistributionFactor import LoadDistributionFactor
from IEC62325.MarketOperations.MktDomain.ApnodeType import ApnodeType
from IEC62325.MarketOperations.MktDomain.ParticipationCategoryMPM import ParticipationCategoryMPM
from IEC62325.MarketOperations.ReferenceData.TACArea import TACArea
from IEC62325.MarketOperations.ReferenceData.Pnode import Pnode
from IEC62325.MarketOperations.ReferenceData.PnodeDistributionFactor import PnodeDistributionFactor



class AggregatedPnode(Pnode):
    """
    An aggregated pricing node is a specialized type of pricing node used to model
    items such as System Zone, Default Price Zone, Custom Price Zone, Control Area,
    Aggregated Generation, Aggregated Particpating Load, Aggregated Non-
    Participating Load, Trading Hub, Designated Control Area(DCA) Zone.
    @created 28-Dec-2023 1:01:42 PM
    """

    def __init__(self) -> None:
        super().__init__()

        # * Aggregate Price Node Types
        self.apnode_type: ApnodeType = ApnodeType()
        # 	 * Designated Control Area participation in LMP price measurement
        # 	 *
        # 	 * 'Y' - Participates in both Local Market Power Mitigation (LMPM) and System
        # 	 * Market Power Mitigation (SMPM)
        # 	 * 'N' - Not included in LMP price measures
        # 	 * 'S' - Participatesin SMPM price measures
        # 	 * 'L' - Participatesin LMPM price measures
        self.participation_category = ParticipationCategoryMPM.N
        self.tac_area = TACArea()
        self.pnode_distribution_factor = PnodeDistributionFactor()
        self.mpm_test_results = MPMTestResults()
        self.gen_distribution_factor = GenDistributionFactor()
        self.load_distribution_factor = LoadDistributionFactor()
