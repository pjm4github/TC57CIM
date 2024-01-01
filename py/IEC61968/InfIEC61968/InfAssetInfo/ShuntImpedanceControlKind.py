# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from enum import Enum

class ShuntImpedanceControlKind(Enum):
    FIXED = 1
    LOCAL_ONLY = 2
    REMOTE_ONLY = 3
    REMOTE_WITH_LOCAL_OVERRIDE = 4
