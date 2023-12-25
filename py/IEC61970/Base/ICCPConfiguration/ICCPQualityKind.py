# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from enum import Enum

class IccpQualityKind(Enum):
    NONE = 1
    QUALITY_ONLY = 2
    QUALITY_AND_TIME = 3
    EXTENDED = 4
    EXTENDED_WITH_QUALITY_TIME = 5
