# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Dec 27 15:35:30 2023
from datetime import datetime

from IEC62325.MarketOperations.MarketOpCommon.MktTerminal import MktTerminal
from IEC62325.MarketOperations.MarketSystem.ExternalInputs.ConstraintTerm import ConstraintTerm


class TerminalConstraintTerm(ConstraintTerm):
    """
    A constraint term associated with a specific terminal on a physical piece of
    equipment.
    @created 27-Dec-2023 3:33:03 PM
    """
    def __init__(self) -> None:
        super().__init__()
        self.mkt_terminal: MktTerminal = MktTerminal()
