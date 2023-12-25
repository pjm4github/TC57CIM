# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# psr_event_kind.py

from enum import Enum

class PSREventKind(Enum):
    IN_SERVICE = 1
    OUT_OF_SERVICE = 2
    PENDING_ADD = 3
    PENDING_REMOVE = 4
    PENDING_REPLACE = 5
    OTHER = 6
    UNKNOWN = 7
