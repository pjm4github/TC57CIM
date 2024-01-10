# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023

from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime


class TradeError:
    """
    Trade error and warning messages associated with the rule engine processing of
    the submitted trade.
    @created 28-Dec-2023 5:24:00 PM
    """

    def __init__(self) -> None:
        """
        Constructor
        """
        self.end_time: Optional[DateTime] = DateTime()   # hour within the trade for which the error applies
        self.err_message: Optional[str] = ""  # error message
        self.err_priority: Optional[int] = 0  # Priority number for the error message
        self.log_time_stamp: Optional[DateTime] = DateTime()   # Timestamp of logged error/warning message
        self.rule_id: Optional[int] = 0  # Rule identifier which triggered the error/warning message
        self.start_time: Optional[DateTime] = DateTime()   # hour within the trade for which the error applies
