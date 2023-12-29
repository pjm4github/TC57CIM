# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 15:17:19 2023
from enum import Enum


class TimeOfUse(Enum):
    """
    Time of Use used by a CRR definition for specifying the time the CRR spans.
    ON - CRR spans the on peak hours of the day, OFF - CRR spans the off peak hours
    of the day, 24HR - CRR spans the entire day.
    """
    ON = 1  # Time of use spans only the on peak hours of the day.
    OFF = 2  # Time of use spans only the off peak hours of the day.
    _24HR = 3  # Time of use spans the entire day, 24 hours.
