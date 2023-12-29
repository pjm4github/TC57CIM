# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class ResourceCapacityType(Enum):
    """
    Resource capacity type.
    """
    RU = 1  # Regulation Up
    RD = 2  # Regulation Down
    SR = 3  # Spinning reserve
    NR = 4  # Non-spinning reserve
    MO = 5  # Must Offer
    FO = 6  # Flexible Offer
    RA = 7  # Resource Adequacy
    RMR = 8  # Reliability Must Run
