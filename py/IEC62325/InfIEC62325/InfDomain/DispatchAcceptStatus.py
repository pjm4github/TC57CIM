# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 19:52:13 2023
from enum import Enum

class DispatchAcceptStatus(Enum):
    NON_RESPONSE = 0
    OK = 1
    CANNOT = 2
    ACCEPT = 3
    DECLINE = 4
    PARTIAL = 5
