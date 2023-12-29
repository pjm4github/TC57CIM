# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class TRType(Enum):
    """
    Transmission Contract Right type - for example:
    individual or chain of contract rights
    """
    CHAIN = 1  # TR chain
    INDIVIDUAL = 2  # Individual TR
