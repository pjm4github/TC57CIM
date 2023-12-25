# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local imports
# enum.py
from enum import Enum

class InspectionAnalogKind(Enum):
    """
    Analogs typically recorded during a field inspection.
    """
    
    SF6_PRESSURE_READING = 0
    AIR_PRESSURE_READING = 1
    AIR_PRESSURE_HP_SYSTEM_READING = 2
    COMPRESSOR_HOUR_METER_READING = 3
    AIR_PRESSURE_LP_SYSTEM_READING = 4
