# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject


class Usage(WorkIdentifiedObject):
    """
    The way material and assets are used to perform a certain type of work task.
    The way is described in text in the inheritied description attribute.
    @created 29-Dec-2023 9:19:13 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.status: Optional[Status] = Status()