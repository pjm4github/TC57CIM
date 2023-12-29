# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Thu Dec 28 17:25:42 2023
from datetime import datetime

from IEC61970.Base.Core.IdentifiedObject import IdentifiedObject
from IEC61970.Base.Domain.DateTime import DateTime


class BidError(IdentifiedObject):

    def __init__(self) -> None:
        super().__init__()
        self.component_type: str = ""
        self.end_time: DateTime = DateTime()
        self.err_message: str = ""
        self.err_priority: int = 0
        self.log_time_stamp: DateTime = DateTime()
        self.msg_level: int = 0
        self.rule_id: int = 0
        self.start_time: DateTime = DateTime()