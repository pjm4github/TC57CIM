# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class RampCurveType(Enum):
    """
    For example:
    0 - Fixed ramp rate independent of rate function unit MW output
    1 - Static ramp rates as a function of unit MW output only
    2 - Dynamic ramp rates as a function of unit MW output and ramping time
    """
    FIXED = 0
    STATIC = 1
    DYNAMIC = 2
