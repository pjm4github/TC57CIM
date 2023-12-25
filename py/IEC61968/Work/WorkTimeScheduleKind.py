# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum


class WorkTimeScheduleKind(Enum):
    
    ESTIMATE = 1  # 'estimate'
    REQUEST = 2  # 'request'
    ACTUAL = 3  # 'actual'
    EARLIEST = 4  # 'earliest'
    LATEST = 5  # 'latest'
    IMMEDIATE = 6  # 'immediate'
