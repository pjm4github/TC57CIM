# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# outage_status_kind.py

from enum import Enum

class OutageStatusKind(Enum):
    CONFIRMED = 1
    PREDICTED = 2
    PARTIALLY_RESTORED = 3
    RESTORED = 4
    CLOSED = 5
