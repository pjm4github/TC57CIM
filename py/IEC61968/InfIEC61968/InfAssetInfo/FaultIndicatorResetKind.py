# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from enum import Enum


class FaultIndicatorResetKind(Enum):
    """
    * Kind of resetting the fault indicators.
    * @author T. Kostic
    * @version 1.0
    * @created 29-Dec-2023 6:24:59 PM
    """
    AUTOMATIC = 0
    MANUAL = 1
    REMOTE = 2
    OTHER = 3

