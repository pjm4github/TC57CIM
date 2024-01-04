# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.OldWorkTask import OldWorkTask
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject
from IEC61968.Work.Work import Work


class WorkFlowStep(WorkIdentifiedObject):
    """
    A pre-defined set of work steps for a given type of work.
    @created 29-Dec-2023 9:20:00 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.sequence_number: Optional[int] = 0  # Used to define dependencies of each work flow step, which is for the instance of WorkTask associated with a given instance of WorkFlow.
        self.status: Optional[Status] = Status()
        self.work_tasks: Optional[OldWorkTask] = OldWorkTask()
        self.work: Optional[Work] = Work()
