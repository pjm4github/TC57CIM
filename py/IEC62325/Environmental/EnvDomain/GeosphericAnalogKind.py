# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum


class GeosphericAnalogKind(Enum):
    """
    Kinds of analogs (floats) measuring a geospheric condition.
    @author ppbr003
    @version 1.0
    @created 25-Dec-2023 9:21:22 PM

    Flash rate in strikes/hour/km^2.
    """
    LIGHTNING_DENSITY = 1
    SEISMIC_EAST_WEST = 2
    SEISMIC_NORTH_SOUTH = 3
    SEISMIC_VERTICAL = 4
    SNOW_PACK_DEPTH = 5
    TEMPERATURE = 6
