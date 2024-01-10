# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.CUGroup import CUGroup
from IEC61968.InfIEC61968.InfWork.ConditionFactor import ConditionFactor
from IEC61968.InfIEC61968.InfWork.Design import Design
from IEC61968.InfIEC61968.InfWork.OldWorkTask import OldWorkTask
from IEC61968.InfIEC61968.InfWork.WorkActionKind import WorkActionKind
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject
from IEC61970.Base.Domain.Date import Date
from IEC61970.Base.Domain.IntegerQuantity import IntegerQuantity


class DesignLocationCU(WorkIdentifiedObject):
    """
    Compatible unit at a given design location.
    @updated 29-Dec-2023 9:15:49 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.cu_account: Optional[str] = ""  # A code1 that helps direct accounting (capital, expense, or accounting treatment).
        self.cu_action: Optional[WorkActionKind] = WorkActionKind.REMOVE  # A code1 that instructs the crew what action to perform.
        self.cu_quantity: Optional[IntegerQuantity] = IntegerQuantity()  # The quantity of the CU being assigned to this location.
        self.cu_usage: Optional[str] = ""  # As the same CU can be used for different purposes and accounting purposes, usage must be specified. Examples include: distribution, transmission, substation.
        self.removal_date: Optional[Date] = Date()  # Year when a CU that represents an asset is removed.
        self.status: Optional[Status] = Status()
        self.to_be_energised: Optional[bool] = True  # True if associated electrical equipment is intended to be energized while work is being performed.
        self.cu_groups: Optional[CUGroup] = CUGroup()
        self.designs: Optional[Design] = Design()
        self.work_tasks: Optional[OldWorkTask] = OldWorkTask()
        self.condition_factors: Optional[ConditionFactor] = ConditionFactor()
