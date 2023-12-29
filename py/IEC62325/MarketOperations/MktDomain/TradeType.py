# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class TradeType(Enum):
    """
    Trade type.
    """
    # InterSC Trade.
    IST = 1
    
    # Ancillary Services Trade.
    AST = 2
    
    # Unit Commitment Trade.
    UCT = 3
