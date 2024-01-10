# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Sat Dec 30 21:42:16 2023
from typing import Optional

from IEC61968.Common.Status import Status
from IEC61968.InfIEC61968.InfWork.ConditionFactorKind import ConditionFactorKind
from IEC61968.InfIEC61968.InfWork.WorkIdentifiedObject import WorkIdentifiedObject


class ConditionFactor(WorkIdentifiedObject):
    """
    This is to specify the various condition factors for a design that may alter
    the cost estimate or the allocation.
    @created 29-Dec-2023 9:13:38 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.cf_value: Optional[
            str] = ""  # The actual value of the condition factor, such as labor flat fee or percentage.
        self.kind = ConditionFactorKind.LABOR  # Kind of this condition factor.
        self.status = Status()
