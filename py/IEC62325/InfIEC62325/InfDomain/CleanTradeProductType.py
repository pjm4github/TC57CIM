# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 19:52:13 2023
from enum import Enum

class CleanTradeProductType(Enum):
    """
    Implementation of the Enumeration CleanTradeProductType
    """

    # Physical Energy Trade
    PHY = 1

    # Energy Trades at Aggregated Pricing Nodes
    APN = 2

    # Converted Physical Energy Trade
    CPT = 3

    # Regulation Up Trade
    RUT = 4

    # Regulation Down Trade
    RDT = 5

    # Spinning Reserve Trade
    SRT = 6

    # Non-Spinning Reserve Trade
    NRT = 7
