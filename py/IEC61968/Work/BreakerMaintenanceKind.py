from enum import Enum


# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
class BreakerMaintenanceKind(Enum):
    EXTERNAL_OUT_OF_SERVICE = 0
    INTERNAL_OUT_OF_SERVICE = 1
    INTERRUPTER_OVERHAUL = 2
