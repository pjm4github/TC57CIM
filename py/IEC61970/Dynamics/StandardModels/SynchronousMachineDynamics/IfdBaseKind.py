# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sun Dec 31 17:07:00 2023
from enum import Enum

class IfdBaseKind(Enum):
    """
    Excitation base system mode.
    @author tsaxton
    @version 1.0
    @created 29-Dec-2023 11:24:19 PM
    """
    # Air gap line mode.  ifdBaseValue is computed, not defined by the user, in this mode.
    IFAG = 1
    # No load system with saturation mode.  ifdBaseValue is computed, not defined by the user, in this mode.
    IFNL = 2
    # Full load system mode.  ifdBaseValue is computed, not defined by the user, in this mode.
    IFFL = 3
