# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class ResourceLimitIndicator(Enum):
    """
    Locational AS Flags indicating whether the Upper or Lower Bound limit of the AS
    regional procurement is binding.
    """
    UPPER = 1
    LOWER = 2
