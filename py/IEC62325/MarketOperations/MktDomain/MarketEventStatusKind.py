# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
"""
Market event status types.
@author mspivbe2
@version 1.0
@created 25-Dec-2023 9:21:22 PM
"""

from enum import Enum

class MarketEventStatusKind(Enum):
    """
    The status of the event is currently in a active state.
    Active (when sysdate is equal or greater than to planned start time)
    """
    active = 1

    """
    The status of the event is currently in a cancelled state.
    Cancelled (stopped before planned start time or planned end time)
    """
    cancelled = 2

    """
    The status of the event is currently in a completed state.
    Complete (when sysdate is equal to the release time)
    """
    completed = 3

    """
    The status of the event is currently in a planned state.
    Planned (sysdate is less than planned start time)
    """
    planned = 4
