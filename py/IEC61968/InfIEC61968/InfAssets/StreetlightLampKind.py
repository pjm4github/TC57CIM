# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Wed Jan  3 14:41:22 2024
from enum import Enum

class StreetlightLampKind(Enum):
    """
    Kind of lamp for the streetlight.
    @author T. Kostic
    @version 1.0
    @created 29-Dec-2023 6:16:20 PM
    """
    HIGH_PRESSURE_SODIUM = 1
    MERCURY_VAPOR = 2
    METAL_HALIDE = 3
    OTHER = 4
