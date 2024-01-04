# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject
from IEC61970.Base.Domain.DateTimeInterval import DateTimeInterval


class ShiftPattern(WorkIdentifiedObject):
    """
    The patterns of shifts worked by people or crews.
    @created 29-Dec-2023 9:18:47 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.assignment_type: Optional[str] = str()  # Type of assignement intended to be worked on this shift, for example, temporary, standard, etc.
        self.cycle_count: Optional[int] = 0  # Number of cycles for a temporary shift.
        self.status: Optional[Status] = Status()
        self.validity_interval: Optional[DateTimeInterval] = DateTimeInterval()  # Date and time interval for which this shift pattern is valid (when it became effective and when it expires).
