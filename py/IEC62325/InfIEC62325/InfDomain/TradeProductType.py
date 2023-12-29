# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 19:52:13 2023
from enum import Enum

class TradeProductType(Enum):
    """
    Implementation of the Enumeration TradeProductType
    """
    PHYSICAL_ENERGY_TRADE = 1
    ENERGY_TRADES_AT_AGGREGATED_PRICING_NODES = 2
    REGULATION_UP_TRADE = 3
    REGULATION_DOWN_TRADE = 4
    SPINNING_RESERVE_TRADE = 5
    NON_SPINNING_RESERVE_TRADE = 6
    CAPACITY_TYPE_TRADE = 7
