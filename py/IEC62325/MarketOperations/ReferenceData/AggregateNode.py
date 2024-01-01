# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 13:18:10 2023
from typing import Optional


from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC62325.MarketOperations.MktDomain.AnodeType import AnodeType
from IEC62325.MarketOperations.ReferenceData.CnodeDistributionFactor import CnodeDistributionFactor
from IEC62325.MarketOperations.ReferenceData.Pnode import Pnode
from IEC62325.MarketOperations.ReferenceData.SubControlArea import SubControlArea


class AggregateNode(IdentifiedObject):
    """
    An aggregated node can define a typed grouping further defined by the AnodeType
    enumeration. Types range from System Zone/Regions to Market Energy Regions to
    Aggregated Loads and Aggregated Generators.
    @created 28-Dec-2023 1:01:30 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.anode_typeOptional[AnodeType] = AnodeType.ACA  # Type of aggregated node
        self.qualif_as_orderOptional[int] = 0
        self.pnodeOptional[Pnode] = Pnode()
        self.cnode_distribution_factorOptional[CnodeDistributionFactor] = CnodeDistributionFactor()
        self.sub_control_areaOptional[SubControlArea] = SubControlArea()
