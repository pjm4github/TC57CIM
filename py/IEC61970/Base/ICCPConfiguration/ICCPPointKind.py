# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:37:34 2023
from enum import Enum

class IccpPointKind(Enum):
    """This specifies the type of ICCP point that is to be conveyed."""
    
    # Indicates that an ICCP discrete type is to be conveyed.
    DISCRETE = 1
    
    # Indicates that an ICCP real type is to be conveyed.
    REAL = 2
    
    # Indicates that an ICCP state type is to be conveyed.
    STATE = 3
    
    # Indicates that an ICCP state supplemental type is to be conveyed.
    STATE_SUPPLEMENTAL = 4
    
    # Indicates that an ICCP single protection event type is to be conveyed.
    SINGLE_PROTECTION_EVENT = 5
    
    # Indicates that an ICCP packed protection event is to be conveyed.
    PACKED_PROTECTION_EVENT = 6
