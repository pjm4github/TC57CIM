# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import StrEnum


class MpmTestOutcome(StrEnum):
    PASSED = 'P'
    FAILED = 'F'
    DISABLED = 'D'
    SKIPPED = 'S'

