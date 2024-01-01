# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 12:28:33 2023
from typing import Optional

from IEC61970.Base.Domain.CostPerEnergyUnit import CostPerEnergyUnit
from IEC61970.Base.Domain.PerCent import PerCent
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource
from IEC62325.MarketOperations.ReferenceData.AggregatedPnode import AggregatedPnode
from IEC62325.MarketOperations.ReferenceData.ResourceCertification import MarketType



class MpmTestThreshold:
    """
    Market Power Mitigation (MPM) test thresholds for resource as well as
    designated congestion areas (DCAs).
    @created 28-Dec-2023 12:16:22 PM
    """

    def __init__(self) -> None:
        self.market_typeOptional[MarketType] = MarketType.DAM  # Market Type (DAM, RTM)
        self.percentOptional[PerCent] = PerCent() # Price Threshold in %
        self.priceOptional[CostPerEnergyUnit] = CostPerEnergyUnit()  # Price Threshold in $/MW
        self.aggregated_pnodeOptional[AggregatedPnode] = AggregatedPnode()
        self.registered_resourceOptional[RegisteredResource] = RegisteredResource()
