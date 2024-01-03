# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from enum import Enum


class JointFillKind(Enum):
    """
    Kind of fill for Joint.
    @author T. Kostic
    @version 1.0
    @created 29-Dec-2023 6:14:05 PM
    """
    NO_FILL_PREFAB = 1
    AIR_NO_FILLING = 2
    PETROLATUM = 3
    ASPHALTIC = 4
    OIL = 5
    BLUEFILL_254 = 6
    NO_VOID = 7
    EPOXY = 8
    INSOLUSEAL = 9
    OTHER = 10
