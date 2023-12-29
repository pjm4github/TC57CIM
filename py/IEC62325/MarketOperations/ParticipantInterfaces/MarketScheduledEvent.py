# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from datetime import timedelta
from enum import Enum

from IEC61968.Common.Status import Status
from IEC61970.Base.Domain.Seconds import Seconds


class MarketScheduledEvent:
    """
    Signifies an event to trigger one or more activities, such as reading a meter,
    recalculating a bill, requesting work, when generating units shall be scheduled
    for maintenance, when a transformer is scheduled to be refurbished, etc.
    @created 28-Dec-2023 5:22:33 PM
    """
    #
    # class Status(Enum):
    #     PENDING = "Pending"
    #     COMPLETED = "Completed"
    #     CANCELLED = "Cancelled"

    def __init__(self) -> None:
        """
        Initializes a new MarketScheduledEvent.
        """
        self.category = ""
        self.duration = Seconds()
        self.status = Status()
