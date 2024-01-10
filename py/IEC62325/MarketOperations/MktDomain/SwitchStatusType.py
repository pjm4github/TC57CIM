# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class SwitchStatusType(Enum):
    """
    Circuit Breaker Status (closed or open) of the circuit breaker.
    """
    CLOSED = 1
    OPEN = 2
