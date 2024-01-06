# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Jan  6 17:13:56 2024
# Enum for dependency type
from enum import StrEnum


class DependencyType(StrEnum):
    # Enum representing the type of dependency
    MUTUALLY_EXCLUSIVE = 'mutually_exclusive'  # Represents mutually exclusive dependency
    REQUIRED = 'required'  # Represents required dependency
