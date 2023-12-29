# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketOperations.MktDomain.AutomaticDispInstTypeCommitment import AutomaticDispInstTypeCommitment
from IEC62325.MarketOperations.MktDomain.CommitmentType import CommitmentType
from IEC62325.MarketOperations.MktDomain.MQSCHGType import MQSCHGType


class Commitments:
    """
    Provides the necessary information (on a resource basis) to capture
    the Startup/Shutdown commitment results. This information is relevant
    to all markets.
    @created 28-Dec-2023 8:19:10 PM
    """

    def __init__(self) -> None:
        self.commitment_type: Optional[CommitmentType] = CommitmentType()
        """
        the type of UC status (self commitment, ISO commitment, or SCUC commitment)
        """
        self.instruction_cost: float = 0.0
        """
        Total cost associated with changing the status of the resource.
        """
        self.instruction_type: Optional[AutomaticDispInstTypeCommitment] = AutomaticDispInstTypeCommitment.START_UP
        """
        Indicator of either a Start-Up or a Shut-Down.
        """
        self.interval_end_time: DateTime = DateTime()
        """
        End time for the commitment period. This will be on an interval boundary.
        """
        self.interval_start_time: DateTime = DateTime()
        """
        Start time for the commitment period. This will be on an interval boundary.
        """
        self.min_status_change_time: str = ""
        """
        SCUC commitment period start-up time. Calculated start up time based on the
        StartUpTimeCurve provided with the Bid. This is a combination of StartUp time
        bid and Unit down time.
        Units is minutes
        """
        self.no_load_cost: float = 0.0
        """
        Unit no load cost in case of energy commodity
        """
        self.update_time_stamp: DateTime = DateTime()
        self.update_type: Optional[MQSCHGType] = MQSCHGType.ADD
        self.update_user: str = ""
