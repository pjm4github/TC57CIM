# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum

class ExecutionType(Enum):
    """
    Execution types of Market Runs.
    """

    DA = 0  # Day Ahead
    HASP = 1  # Real TIme Hour Ahead Execution
    RTPD = 2  # Real Time Pre-dispatch
    RTD = 3  # Real Time Dispatch
