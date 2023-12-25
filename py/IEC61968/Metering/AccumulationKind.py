# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum


class AccumulationKind(Enum):
    NONE = 1  # " NONE"
    BULK_QUANTITY = 2  # " bulkQuantity"
    CONTINUOUS_CUMULATIVE = 3  # " continuousCumulative"
    CUMULATIVE = 4  # " Cumulative"
    DELTA_DATA = 5  # " DeltaData"
    INDICATING = 6  # " Indicating"
    SUMMATION = 7  # " SUmmation"
    TIME_DELAY = 8  # " TimeDelay"
    INSTANTANEOUS = 9  # " instantaneous"
    LATCHING_QUANTITY = 10  # " latchingQuantity"
    BOUNDED_QUANTITY = 11  # " boundedQuantity"

