# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
"""
Kind of Market account.
@author T. Kostic
@version 1.0
@created 25-Dec-2023 9:21:22 PM
"""
from enum import Enum


class MktAccountKind(Enum):
    NORMAL = 1
    REVERSAL = 2
    STATISTICAL = 3
    ESTIMATE = 4
