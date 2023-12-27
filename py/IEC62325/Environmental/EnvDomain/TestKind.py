# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local import
# The test applied to determine if the condition is met.
# @author ppbr003
# @version 1.0
# @created 25-Dec-2023 9:21:23 PM
from enum import Enum


# converting java enum to python class
class TestKind(Enum):
    EQUAL_TO = 0
    GREATER_THAN = 1
    LESS_THAN = 2
    GREATER_THAN_OR_EQUAL_TO = 3
    LESS_THAN_OR_EQUAL_TO = 4
