# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors
from IEC62325.MarketOperations.MarketSystem.MarketResults.DopInstruction import DopInstruction


class InstructionClearingDop(MarketFactors):
    def __init__(self) -> None:
        super().__init__()
        self.dop_instruction: DopInstruction()
