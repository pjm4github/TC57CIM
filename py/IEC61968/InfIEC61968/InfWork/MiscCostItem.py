# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.WorkCostDetail import WorkCostDetail
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject
from IEC61970.Base.Domain.IntegerQuantity import IntegerQuantity
from IEC61970.Base.Domain.Money import Money


class MiscCostItem(WorkIdentifiedObject):
    """
    Various cost items that are not associated with compatible units. Examples
    include rental equipment, labor, materials, contractor costs, permits -
    anything not covered in a CU.
    @created 29-Dec-2023 9:16:41 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.account: Optional[str] = str()  # This drives the accounting treatment for this misc. item.
        self.cost_per_unit: Optional[Money] = Money()  # The cost per unit for this misc. item.
        self.cost_type: Optional[str] = str()  # The cost type for accounting, such as material, labor, vehicle, contractor, equipment, overhead.
        self.external_ref_id: Optional[str] = str()  # External reference identifier (e.g. purchase order number, serial number).
        self.quantity: Optional[IntegerQuantity] = IntegerQuantity()  # The quantity of the misc. item being assigned to this location.
        self.status: Optional[Status] = Status()
        self.work_cost_detail: Optional[WorkCostDetail] = WorkCostDetail()