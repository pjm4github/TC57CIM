# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class MarketProductSelfSchedType(Enum):
    ETC = 1  # Existing Transmission Contract
    TOR = 2  # Transmission Ownership Right
    RMR = 3  # Reliability Must Run
    RGMR = 4  # Regulatory must run
    RMT = 5  # Reliability must take
    PT = 6  # Price taker
    LPT = 7  # Low price taker
    SP = 8  # Self provision
    RA = 9  # Resource adequacy
