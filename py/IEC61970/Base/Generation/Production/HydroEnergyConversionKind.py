# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:36:32 2023
from enum import Enum

class HydroEnergyConversionKind(Enum):
    """
    Specifies the capability of the hydro generating unit to convert energy as a
    generator or pump.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:27 PM
    """
    # Able to generate power, but not able to pump water for energy storage.
    GENERATOR = 1
    
    # Able to both generate power and pump water for energy storage.
    PUMP_AND_GENERATOR = 2
