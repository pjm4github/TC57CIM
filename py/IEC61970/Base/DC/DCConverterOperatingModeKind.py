# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:22:57 2023
from enum import Enum

class DCConverterOperatingModeKind(Enum):
    """The operating mode of an HVDC bipole."""
    
    # Bipolar operation.
    BIPOLAR = 0
    
    # Monopolar operation with metallic return
    MONOPOLAR_METALLIC_RETURN = 1
    
    # Monopolar operation with ground return
    MONOPOLAR_GROUND_RETURN = 2
