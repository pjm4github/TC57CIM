# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum

class SinglePhaseKind(Enum):
    """
    Enumeration of single phase identifiers. Allows designation of single phases for both
    transmission and distribution equipment, circuits and loads.
    """
    A = 1  # Phase A.
    B = 2  # Phase B.
    C = 3  # Phase C.
    N = 4  # Neutral.
    S1 = 5  # Secondary phase 1.
    S2 = 6  # Secondary phase 2.
