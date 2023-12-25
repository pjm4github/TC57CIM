# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 15 17:33:10 2023
from typing import Any, Optional

from CIM_STD_PYTHON.TC57CIM.IEC61970.Base.Domain.DateTime import DateTime


class DateInterval:
    """
    Interval between two dates.
    @author T. Kostic
    @version 1.0
    @created 15-Dec-2023 4:38:26 PM
    """

    def __init__(self) -> None:
        self.start: Optional[DateTime] = None  #  Start date of this interval.
        self.end: Optional[DateTime] = None  #  End date of this interval.
