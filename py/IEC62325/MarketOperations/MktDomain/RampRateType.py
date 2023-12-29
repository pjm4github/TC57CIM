# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class RampRateType(Enum):
    """
    Ramp rate curve type.
    """
    OP = 1   # Operational ramp rate.
    REG = 2  # Regulating ramp rate.
    OP_RES = 3  # Operating reserve ramp rate.
    LD_DROP = 4  # Load drop ramp rate.
    LD_PICKUP = 5  # Load pick up rate.
    INTERTIE = 6  # Intertie ramp rate.
