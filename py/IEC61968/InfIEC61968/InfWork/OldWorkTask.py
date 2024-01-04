from typing import Optional

from IEC61968.InfIEC61968.InfWork.ContractorItem import ContractorItem
from IEC61968.InfIEC61968.InfWork.LaborItem import LaborItem
from IEC61968.InfIEC61968.InfWork.MiscCostItem import MiscCostItem
from IEC61968.InfIEC61968.InfWork.OverheadCost import OverheadCost
from IEC61968.InfIEC61968.InfWork.QualificationRequirement import QualificationRequirement
from IEC61968.InfIEC61968.InfWork.Usage import Usage
from IEC61968.Work.WorkTask import WorkTask


class OldWorkTask(WorkTask):
    """
    A set of tasks is required to implement a design.
    @created 29-Dec-2023 9:17:06 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.labor_items: Optional[LaborItem] = LaborItem()
        self.overhead_cost: Optional[OverheadCost] = OverheadCost()
        self.qualification_requirements: Optional[QualificationRequirement] = QualificationRequirement()
        self.misc_cost_items: Optional[MiscCostItem] = MiscCostItem()
        self.usages: Optional[Usage] = Usage()
        self.contractor_items: Optional[ContractorItem] = ContractorItem()
