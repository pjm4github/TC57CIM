# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# local imports
from enum import Enum


class AnalyticKind(Enum):
    RISK_ANALYTIC = 1
    FAULT_ANALYTIC = 2
    AGING_ANALYTIC = 3
    HEALTH_ANALYTIC = 4
    REPLACEMENT_ANALYTIC = 5
    OTHER = 6
