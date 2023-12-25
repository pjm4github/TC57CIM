# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum

class SynchronousMachineKind(Enum):
    GENERATOR = 1
    CONDENSER = 2
    GENERATOR_OR_CONDENSER = 3
    MOTOR = 4
    GENERATOR_OR_MOTOR = 5
    MOTOR_OR_CONDENSER = 6
    GENERATOR_OR_CONDENSER_OR_MOTOR = 7
