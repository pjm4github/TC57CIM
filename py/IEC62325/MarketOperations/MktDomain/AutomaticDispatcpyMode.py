# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class AutomaticDispatchMode(Enum):
    INTERVAL = 1  # Contingnency occurance, redispatch of contingency reserves
    CONTINGENCY = 2
    MANUAL = 3
