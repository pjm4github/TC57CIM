# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class SelfSchedReferenceType(Enum):
    """
    Indication of which type of self schedule is being referenced.
    """
    ETC = 1  # Existing transmission contract.
    TOR = 2  # Transmission ownership right.
