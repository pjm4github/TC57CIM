# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from enum import Enum


class CoolingKind(Enum):
    """
    Kind of cooling.
    @author T. Kostic
    @version 1.0
    @created 29-Dec-2023 6:13:36 PM
    """
    SELF_COOLING = 1
    FORCED_AIR = 2
    FORCED_OIL_AND_AIR = 3
    OTHER = 4
