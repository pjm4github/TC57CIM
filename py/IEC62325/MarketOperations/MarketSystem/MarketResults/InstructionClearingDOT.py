# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors
from IEC62325.MarketOperations.MarketSystem.MarketResults.DotInstruction import DotInstruction
from IEC62325.MarketOperations.MktDomain.AutomaticDispatcpyMode import AutomaticDispatchMode
from IEC62325.MarketOperations.MktDomain.YesNo import YesNo


class InstructionClearingDOT(MarketFactors):
    
    def __init__(self) -> None:
        super().__init__()
        self.contingency_active: Optional[YesNo] = YesNo.NO
        self.dispatch_mode: Optional[AutomaticDispatchMode] = AutomaticDispatchMode.MANUAL
        self.dot_instruction: Optional[DotInstruction] = DotInstruction()
