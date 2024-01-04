# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.InfIEC61968.InfERPSupport.ErpBOM import ErpBOM
from IEC61968.InfIEC61968.InfWork.ConditionFactor import ConditionFactor
from IEC61968.InfIEC61968.InfWork.DesignKind import DesignKind
from IEC61968.InfIEC61968.InfWork.OldWorkTask import OldWorkTask
from IEC61968.InfIEC61968.InfWork.WorkCostDetail import WorkCostDetail
from IEC61968.InfIEC61968.InfWork.WorkDocument import WorkDocument
from IEC61968.Work.Work import Work
from IEC61970.Base.Domain.Money import Money


class Design(WorkDocument):
    """
    A design for consideration by customers, potential customers, or internal work.

    Note that the Version of design is the revision attribute that is inherited
    from Document.
    @created 29-Dec-2023 9:14:12 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.cost_estimate: Optional[Money] = Money()  # Estimated cost (not price) of design.
        self.kind: Optional[DesignKind] = DesignKind.ESTIMATED  # Kind of this design.
        self.price: Optional[Money] = Money()  # Price to customer for implementing design.
        self.work_cost_details = [WorkCostDetail()]
        self.erp_boms = [ErpBOM()]
        self.work_tasks = [OldWorkTask()]
        self.condition_factors = [ConditionFactor()]
        self.work: Optional[Work] = Work()