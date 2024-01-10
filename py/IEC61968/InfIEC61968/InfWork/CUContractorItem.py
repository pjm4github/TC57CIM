# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.CompatibleUnit import CompatibleUnit
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject
from IEC61970.Base.Domain.Money import Money


class CUContractorItem(WorkIdentifiedObject):
    """
    Compatible unit contractor item.
    """

    def __init__(self) -> None:
        super().__init__()
        self.activity_code: Optional[str] = ""  # Activity code1 identifies a specific and distinguishable unit of work.
        self.bid_amount: Optional[Money] = Money()  # The amount that a given contractor will charge for performing this unit of work.
        self.status: Optional[Status] = Status()
        self.compatible_units: Optional[CompatibleUnit] = CompatibleUnit()
