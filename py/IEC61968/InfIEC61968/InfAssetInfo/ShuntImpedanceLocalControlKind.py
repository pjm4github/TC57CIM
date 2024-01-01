# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 15:58:51 2023
from enum import Enum


class ShuntImpedanceLocalControlKind(Enum):
    NONE = 0
    POWER_FACTOR = 1
    TIME = 2
    TEMPERATURE = 3
    REACTIVE_POWER = 4
    CURRENT = 5
    VOLTAGE = 6
