# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject


class CULaborCode(WorkIdentifiedObject):
    """
    Labor code1 associated with various compatible unit labor items.
    @created 29-Dec-2023 9:12:22 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.code: Optional[str] = ""
        self.status: Optional[Status] = Status()