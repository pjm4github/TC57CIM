# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Import local modules
from enum import Enum


class AggregateKind(Enum):
    NONE = 1  # " None"
    AVERAGE = 2  # " average"
    EXCESS = 3  # " excess"
    HIGH_THRESHOLD = 4  # " high_threshold"
    LOW_THRESHOLD = 5  # " low_threshold"
    MAXIMUM = 6  # " maximum"
    MINIMUM = 7  # " minimum"
    NOMINAL = 8  # " nominal"
    NORMAL = 9  # " normal"
    SECOND_MAXIMUM = 10  # " second_maximum"
    SECOND_MINIMUM = 11  # " second_minimum"
    THIRD_MAXIMUM = 12  # " third_maximum"
    FOURTH_MAXIMUM = 13  # " fourth_maximum"
    FIFTH_MAXIMUM = 14  # " fifth_maximum"
    SUM = 15  # " Sum"
