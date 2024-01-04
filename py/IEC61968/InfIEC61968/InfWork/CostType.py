# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfERPSupport.ErpJournalEntry import ErpJournalEntry
from IEC61968.InfIEC61968.InfWork.CompatibleUnit import CompatibleUnit
from IEC61968.InfIEC61968.InfWork.WorkCostDetail import WorkCostDetail
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject


class CostType(WorkIdentifiedObject):
    """
    A categorization for resources, often costs, in accounting transactions.
    Examples include: material components, building in service, coal sales,
    overhead, etc.
    @created 29-Dec-2023 9:14:02 PM
    """

    def __init__(self) -> None:
        super().__init__()
        """
        True if an amount can be assigned to the resource element (e.g., building in
        service, transmission plant, software development capital); false otherwise (e.
        g., internal labor, material components).
        """
        self.amount_assignable: Optional[bool] = True

        """
        A codified representation of the resource element.
        """
        self.code: Optional[str] = ""

        """
        The level of the resource element in the hierarchy of resource elements
        (recursive relationship).
        """
        self.level: Optional[str] = ""

        """
        The stage for which this costType applies: estimated design, estimated actual
        or actual actual.
        """
        self.stage: Optional[str] = ""

        self.status: Optional[Status] = Status()
        self.child_cost_types: Optional[CostType] = CostType()
        self.work_cost_details: Optional[WorkCostDetail] = WorkCostDetail()
        self.erp_journal_entries: Optional[ErpJournalEntry] = ErpJournalEntry()
        self.compatible_units: Optional[CompatibleUnit] = CompatibleUnit()

