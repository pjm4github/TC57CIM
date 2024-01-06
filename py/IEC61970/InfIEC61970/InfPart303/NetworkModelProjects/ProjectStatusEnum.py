# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 17:13:56 2024
# public enum ProjectStatusEnum {
from enum import StrEnum


class ProjectStatusEnum(StrEnum):
    # draft,
    DRAFT = 'draft'
    # cancelled,
    CANCELLED = 'cancelled'
    # frozen,
    FROZEN = 'frozen'
    # closed
    CLOSED = 'closed'
    
