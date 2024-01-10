# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 19:52:13 2023
from enum import Enum


class BidStatusType(Enum):
    CL = 1  # Clean
    RP = 2  # Replicated
    RJ = 3  # Rejected
    I = 4  # Invalid
    CV = 5  # Conditionally Valid
    CM = 6  # Conditionally Modified
    V = 7  # Valid
    M = 8  # Modified
    CX = 9  # Cancelled
    O = 10  # Obsolete
