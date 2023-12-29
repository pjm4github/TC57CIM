# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class ContractType(Enum):
    """
    Transmission Contract Type, For example:
    O - Other
    TE - Transmission Export
    TI - Transmission Import
    ETC - Existing Transmission Contract
    RMT - RMT Contract
    TOR - Transmission Ownership Right
    RMR - Reliability Must Run Contract
    CVR - Converted contract
    """
    ETC = 1  # Existing Transmission Contract
    TOR = 2  # Transmission Ownership Right
    RMR = 3  # Reliability Must Run Contract
    RMT = 4  # RMT Contract
    O = 5    # Other
    TE = 6   # Transmission Export
    TI = 7   # Transmission Import
    CVR = 8  # Converted contract
