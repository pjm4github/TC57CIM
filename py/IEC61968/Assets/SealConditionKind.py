# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# seal_condition_kind.py

from enum import Enum

class SealConditionKind(Enum):
    LOCKED = 1
    OPEN = 2
    BROKEN = 3
    MISSING = 4
    OTHER = 5
