# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class DispatchResponseType(Enum):
    """
    For example:
    NON_RESPONSE
    ACCEPT
    DECLINE
    PARTIAL
    """
    NON_RESPONSE = 0
    ACCEPT = 1
    DECLINE = 2
    PARTIAL = 3
