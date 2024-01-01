# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 22:01:48 2023
from enum import Enum

class ExcREXSFeedbackSignalKind(Enum):
    FIELD_VOLTAGE = 1  # The voltage regulator output voltage is used. It is the same as exciter field voltage.
    FIELD_CURRENT = 2  # The exciter field current is used.
    OUTPUT_VOLTAGE = 3  # The output voltage of the exciter is used.
