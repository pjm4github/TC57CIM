# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Local import
# from CIM_STD_PYTHON.TC57CIM.IEC61968.AssetInfo import ...
from enum import Enum


# Enum class
class InterruptingMediumKind(Enum):
    AIR_BLAST = 1  # "AIRBLAST"
    AIR_MAGNETIC = 2  # "AIRMAGNETIC"
    GAS_TWO_PRESSURE = 3  # "GASTWOPRESSURE"
    GAS_SINGLE_PRESSURE = 4  # "GASSINGLEPRESSURE"
    BULK_OIL = 5  # "BULKOIL"
    MINIMUM_OIL = 6  # "MINIMUMOIL"
    VACUUM = 7  # "VACUUM"
