# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.InfIEC61968.InfERPSupport.ErpProjectAccounting import ErpProjectAccounting
from IEC61968.InfIEC61968.InfWork.ContractorItem import ContractorItem
from IEC61968.InfIEC61968.InfWork.OldWorkTask import OldWorkTask
from IEC61968.InfIEC61968.InfWork.PropertyUnit import PropertyUnit
from IEC61968.InfIEC61968.InfWork.WorkCostSummary import WorkCostSummary
from IEC61968.InfIEC61968.InfWork.WorkDocument import WorkDocument
from IEC61968.Work.Work import Work
from IEC61970.Base.Domain.DateTime import DateTime
from IEC61970.Base.Domain.Money import Money


class WorkCostDetail(WorkDocument):
    """
    A collection of all the individual cost items collected from multiple
    sources.
    @created 29-Dec-2023 9:19:35 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.amount: Optional[Money] = Money()  # Amount in designated currency for work, either a total or an individual element. As defined in the attribute "type," multiple instances are applicable to each work for: planned cost, actual cost, authorized cost, budgeted cost, forecasted cost, other.
        self.is_debit: Optional[bool] = True  # True if 'amount' is a debit, false if it is a credit.
        self.transaction_date_time: Optional[DateTime] = DateTime()  # Date and time that 'amount' is posted to the work.
        self.erp_project_accounting: Optional[ErpProjectAccounting] = ErpProjectAccounting()
        self.contractor_items: Optional[ContractorItem] = ContractorItem()
        self.work_cost_summary: Optional[WorkCostSummary] = WorkCostSummary()
        self.property_units: Optional[PropertyUnit] = PropertyUnit()
        self.work_task: Optional[OldWorkTask] = OldWorkTask()
        self.works: Optional[Work] = Work()
