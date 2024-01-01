# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

from IEC62325.MarketCommon.RegisteredResource import RegisteredResource
from IEC62325.MarketOperations.MarketSystem.MarketResults.ExPostResource import ExPostResource
from IEC62325.MarketOperations.MktDomain.EquipmentStatusType import EquipmentStatusType


class ExPostResourceResults:
    """
    Model of ex-post pricing of resources contains components of LMPs: energy,
    congestion, loss. Resource based.
    @created 28-Dec-2023 8:21:11 PM
    """

    def __init__(self) -> None:
        self.congestion_lmp: float = 0.0  # LMP component in USD (deprecated)
        self.desired_mw: float = 0.0  # Desired output of unit
        self.dispatch_rate: float = 0.0  # Unit Dispatch rate from real time unit dispatch
        self.lmp: float = 0.0  # LMP (Local Marginal Price) in USD at the equipment (deprecated)
        self.loss_lmp: float = 0.0  # loss lmp (deprecated)
        self.max_economic_mw: float = 0.0  # Economic Maximum MW
        self.min_economic_mw: float = 0.0  # Economic Minimum MW
        self.resource_mw: float = 0.0  # Current MW output of the equipment
        self.statusOptional[EquipmentStatusType] = EquipmentStatusType()  # Status of equipment
        self.ex_post_resourceOptional[ExPostResource] = ExPostResource()
        self.registered_resourceOptional[RegisteredResource] = RegisteredResource()
