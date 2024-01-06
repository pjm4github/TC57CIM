# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class CRRSegmentType(Enum):
    """
    Type of the CRR, from the possible type definitions in the CRR System (e.g.
    'LSE', 'ETC').
    """
    AUC = 1
    CAP = 2
    CF = 3
    CVR = 4  # Converted rights.
    ETC = 5  # Existing Transmission Contract.
    LSE = 6  # Load Serving Entity.
    MT = 7  # Merchant transmission.
    TOR = 8  # Transmission Ownership Rights.
