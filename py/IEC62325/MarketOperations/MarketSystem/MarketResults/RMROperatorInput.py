# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional


from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MarketPlan.MarketFactors import MarketFactors
from IEC62325.MarketOperations.MktDomain.MQSCHGType import MQSCHGType


class RMROperatorInput(MarketFactors):

    """
    RMR Operator's entry of the RMR requirement per market interval.
    @created 28-Dec-2023 8:25:02 PM
    """

    def __init__(self) -> None:
        super().__init__()
        self.manually_sched_rmrmw: float = 0.0  # The lower of the original pre-dispatch or the AC run schedule (Also known as the RMR Reguirement) becomes the pre-dispatch value.
        self.update_time_stamp: DateTime = DateTime()
        self.update_type: Optional[MQSCHGType] = MQSCHGType.ADD
        self.update_user: str = ""
