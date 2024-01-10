# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.WorkCostDetail import WorkCostDetail
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject
from IEC61970.Base.Domain.CostRate import CostRate
from IEC61970.Base.Domain.Hours import Hours
from IEC61970.Base.Domain.Money import Money


class LaborItem(WorkIdentifiedObject):
    """
    Labor used for work order.
    @created 29-Dec-2023 9:16:27 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.activity_code: Optional[str] = str()  # Activity code1 identifies a specific and distinguishable unit of work.
        self.cost: Optional[Money] = Money()  # Total cost for labor. Note that this may not be able to be derived from labor rate and time charged.
        self.labor_duration: Optional[Hours] = Hours()  # Time required to perform work.
        self.labor_rate: Optional[CostRate] = CostRate()  # The labor rate applied for work.
        self.status: Optional[Status] = Status()
        self.work_cost_detail: Optional[WorkCostDetail] = WorkCostDetail()
