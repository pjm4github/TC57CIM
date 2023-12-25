# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
from enum import Enum

class WorkStatusKind(Enum):
    WAITING_ON_APPROVAL = 1
    APPROVED = 2
    CANCELLED = 3
    WAITING_TO_BE_SCHEDULED = 4
    SCHEDULED = 5
    WAITING_ON_MATERIAL = 6
    IN_PROGRESS = 7
    COMPLETED = 8
    CLOSED = 9
    DISPATCHED = 10
    EN_ROUTE = 11
    ON_SITE = 12
