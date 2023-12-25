# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:02:59 2023
from enum import Enum

class ControlAreaTypeKind(Enum):
    """The type of control area."""
    
    # Used for automatic generation control.
    AGC = 0  
    
    # Used for load forecast.
    FORECAST = 1
    
    # Used for interchange specification or control.
    INTERCHANGE = 2
