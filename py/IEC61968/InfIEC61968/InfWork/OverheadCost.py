# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.WorkCostDetail import WorkCostDetail
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject
from IEC61970.Base.Domain.Money import Money


class OverheadCost(WorkIdentifiedObject):
    """
    Overhead cost applied to work order.
    @created 29-Dec-2023 9:17:36 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.code: Optional[str] = str()  # Overhead code1.
        self.cost: Optional[Money] = Money()  # The overhead cost to be applied.
        self.status: Optional[Status] = Status()
        self.work_cost_details: Optional[WorkCostDetail] = WorkCostDetail()