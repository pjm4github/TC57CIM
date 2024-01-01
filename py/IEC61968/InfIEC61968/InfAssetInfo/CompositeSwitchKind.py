# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from enum import Enum

class CompositeSwitchKind(Enum):
    """
    Kind of composite switch.
    @author T. Kostic
    @version 1.0
    @created 29-Dec-2023 6:23:55 PM
    """
    THROW_OVER = 1
    ESCO_THROW_OVER = 2
    RAL = 3
    GRAL = 4
    REGULATOR_BYPASS = 5
    UG_MULTI_SWITCH = 6
    OTHER = 7
