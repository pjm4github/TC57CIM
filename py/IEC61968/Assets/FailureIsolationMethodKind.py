# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# failure_isolation_method_kind.py

from enum import Enum

class FailureIsolationMethodKind(Enum):
    BREAKER_OPERATION = 1
    FUSE = 2
    BURNED_IN_THE_CLEAR = 3
    MANUALLY_ISOLATED = 4
    OTHER = 5
