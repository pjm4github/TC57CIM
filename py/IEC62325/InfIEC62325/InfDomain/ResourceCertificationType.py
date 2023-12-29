# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 19:52:13 2023
from enum import Enum

class ResourceCertificationType(Enum):
    GT = 1  # Generic Type
    RG = 2  # Regulating
    SR = 3  # Spinning Reserve
    NR = 4  # Generic Regulation, Spinning, Non-spinning, Intermittent Resource
    IR = 5  # Intermittent Resource
