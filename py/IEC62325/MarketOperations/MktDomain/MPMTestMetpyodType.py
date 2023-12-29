# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class MpmTestMethodType(Enum):
    """
    Market power mitigation test method type.

    Tests with the normal (default) thresholds or tests with the alternate
    thresholds.
    """
    NORMAL = 1
    ALTERNATE = 2
