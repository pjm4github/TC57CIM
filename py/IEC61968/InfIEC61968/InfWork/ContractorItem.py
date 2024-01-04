# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfERPSupport.ErpPayable import ErpPayable
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject
from IEC61970.Base.Domain.Money import Money


class ContractorItem(WorkIdentifiedObject):
    """
    Contractor information for work task.
    @created 29-Dec-2023 9:13:50 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.activity_code: str = ""
        """
        Activity code identifies a specific and distinguishable unit of work.
        """

        self.bid_amount: Money = Money()
        """
        The amount that a given contractor will charge for performing this unit of work.
        """

        self.cost: Money = Money()
        """
        The total amount charged.
        """

        self.status: Status = Status()
        self.erp_payables = ErpPayable()
