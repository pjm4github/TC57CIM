# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum

class MeterMultiplierKind(Enum):
    KH = 1  # "kH" # Meter kh (watthour) constant. The number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter.
    KR = 2  # "kR" # Register multiplier. The number to multiply the register reading by in order to get kWh.
    KE = 3  # "kE" # Test constant.
    CT_RATIO = 4  # "ctRatio" # Current transformer ratio used to convert associated quantities to real measurements.
    PT_RATIO = 5  # "ptRatio" # Potential transformer ratio used to convert associated quantities to real measurements.
    TRANSFORMER_RATIO = 6  # "transformerRatio" # Product of the CT ratio and PT ratio.
