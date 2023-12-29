# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 19:52:13 2023
from enum import Enum

class OasisStatusType(Enum):
    DATA_TRANSFER_PROCEDURE_INITIATED = 0
    VALID = 1
    OBSOLETE = 2
    DATA_TRANSFER_SUCCESSFUL = 3
    PUSH_FAILED = 4
    FORCED_TERMINATION = 5
