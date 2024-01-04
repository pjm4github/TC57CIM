# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject


class CUGroup(WorkIdentifiedObject):
    """
    A Compatible Unit Group identifies a set of compatible units which may be
    jointly utilized for estimating and designating jobs.
    @created 29-Dec-2023 9:12:11 PM
    """

    def __init__(self) -> None:
        self.status: Optional[Status] = Status()
        self.child_cu_groups: Optional[CUGroup] = CUGroup()

        super().__init__()