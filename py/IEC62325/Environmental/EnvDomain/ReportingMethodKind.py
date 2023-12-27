# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
# Import statements not required in python
from enum import Enum


# Method by which information is gathered from station.
# @author ppbr003
# @version 1.0
# @created 25-Dec-2023 9:21:23 PM

class ReportingMethodKind(Enum):
    # Station automatically reports.
    AUTOMATED = 1

    # Station must be queried to obtain observations.
    QUERIED = 2

    # Station must be physically visited to gather observations.
    MANUAL = 3
