# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:39:55 2023
from enum import Enum

class OperationalLimitDirectionKind(Enum):
    """
    The direction attribute describes the side of a limit that is a violation.
    @author kdd
    @version 1.0
    @created 15-Dec-2023 4:38:28 PM
    """

    # High means that a monitored value above the limit value is a violation. If applied to a terminal flow, the positive direction is into the terminal.
    HIGH = 1

    # Low means a monitored value below the limit is a violation. If applied to a terminal flow, the positive direction is into the terminal.
    LOW = 2

    # An absoluteValue limit means that a monitored absolute value above the limit value is a violation.
    ABSOLUTE_VALUE = 3
