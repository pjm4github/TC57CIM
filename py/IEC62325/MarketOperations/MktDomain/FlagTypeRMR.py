# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import StrEnum


class FlagTypeRMR(StrEnum):
    N = 'N'  # not an RMR unit
    CONDITION_1 = '1'  # RMR Condition 1 unit
    CONDITION_2 = '2'  # RMR Condition 2 unit
