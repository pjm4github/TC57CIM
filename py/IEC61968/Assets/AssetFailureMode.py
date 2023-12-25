# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# asset_failure_mode.py
from enum import Enum


class AssetFailureMode(Enum):
    FAIL_TO_CARRY_LOAD = 1
    FAIL_TO_CLOSE = 2
    FAIL_TO_INTERRUPT = 3
    FAIL_TO_OPEN = 4
    FAIL_TO_PROVIDE_INSULATION_LEVEL = 5
