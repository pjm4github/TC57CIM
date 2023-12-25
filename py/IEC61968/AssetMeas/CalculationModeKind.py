# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# asset_meas.py
from enum import Enum


class CalculationModeKind(Enum):
    total = 1  # "total"
    period = 2  # "period"
    sliding = 3  # "sliding"
