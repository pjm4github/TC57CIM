# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum


class PetersenCoilModeKind(Enum):
    """The mode of operation for a Petersen coil."""
    
    # Fixed position.
    FIXED = 1
    
    # Manual positioning.
    MANUAL = 2
    
    # Automatic positioning.
    AUTOMATIC_POSITIONING = 3
