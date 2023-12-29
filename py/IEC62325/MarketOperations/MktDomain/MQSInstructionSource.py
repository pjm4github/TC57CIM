# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class MqsInstructionSource(Enum):
    """
    Valid values, for example:
    INS - Instruction from RTM
    ACT - Actual instruction after the fact
    """
    INS = 1
    ACT = 2
