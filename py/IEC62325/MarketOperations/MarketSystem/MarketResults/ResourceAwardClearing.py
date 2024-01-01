# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors
from IEC62325.MarketOperations.MarketSystem.MarketResults.RUCAwardInstruction import RUCAwardInstruction
from IEC62325.MarketOperations.MarketSystem.MarketResults.ResourceAwardInstruction import ResourceAwardInstruction
from IEC62325.MarketOperations.MktDomain.AutomaticDispatcpyMode import AutomaticDispatchMode
from IEC62325.MarketOperations.MktDomain.YesNo import YesNo


class ResourceAwardClearing(MarketFactors):
    """
    Models details of bid and offer market clearing. Class indicates whether a
    contingency is active and whether the automatic dispatching system is active
    for this interval of the market solution.
    @created 28-Dec-2023 8:25:21 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.contingency_activeOptional[YesNo] = YesNo.NO
        self.dispatch_modeOptional[AutomaticDispatchMode] = AutomaticDispatchMode.MANUAL
        self.ruc_award_instructionOptional[RUCAwardInstruction] = RUCAwardInstruction()
        self.resource_award_instructionOptional[ResourceAwardInstruction] = ResourceAwardInstruction()
