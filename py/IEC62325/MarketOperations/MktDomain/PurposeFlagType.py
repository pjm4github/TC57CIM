# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class PurposeFlagType(Enum):
    """
    MPM Purpose Flag, for example:
    *
    Nature of threshold data:
    'M' - Mitigation threshold
    'R' - Reporting threshold
    """
    M = 1
    R = 2
