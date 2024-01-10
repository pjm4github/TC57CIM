# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from IEC62325.MarketCommon.MarketParticipant import MarketParticipant
from IEC62325.MarketOperations.MarketOpCommon.MktConnectivityNode import MktConnectivityNode
from IEC62325.MarketOperations.MarketPlan.CommodityDefinition import CommodityDefinition
from IEC62325.MarketOperations.ReferenceData.AdjacentCASet import AdjacentCASet
from IEC62325.MarketOperations.ReferenceData.AggregateNode import AggregateNode
from IEC62325.MarketOperations.ReferenceData.ContractRight import ContractRight
from IEC62325.MarketOperations.ReferenceData.FuelRegion import FuelRegion
from IEC62325.MarketOperations.ReferenceData.HostControlArea import HostControlArea
from IEC62325.MarketOperations.ReferenceData.LocalReliabilityArea import LocalReliabilityArea
from IEC62325.MarketOperations.ReferenceData.Pnode import Pnode
from IEC62325.MarketOperations.ReferenceData.SubControlArea import SubControlArea
from IEC62325.MarketOperations.ReferenceData.TransmissionRightChain import TransmissionRightChain


class RTO(MarketParticipant):
    def __init__(self) -> None:
        super().__init__()
        self.adjacent_ca_set = AdjacentCASet()
        self.local_reliability_area = LocalReliabilityArea()
        self.fuel_region = FuelRegion()
        self.transmission_contract_right = ContractRight()
        self.aggregate_node = AggregateNode()
        self.host_control_area = HostControlArea()
        self.pnodes = Pnode()
        self.transmission_right_chain = TransmissionRightChain()
        self.sub_control_area = SubControlArea()
        self.commodity_definition = CommodityDefinition()
        self.mkt_connectivity_node = MktConnectivityNode()
