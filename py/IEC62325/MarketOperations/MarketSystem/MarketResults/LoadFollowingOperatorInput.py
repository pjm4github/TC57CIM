# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource
from IEC62325.MarketOperations.MktDomain.MQSCHGType import MQSCHGType


class LoadFollowingOperatorInput:
    """
    Model of load following capabilities that are entered by operators on a
    temporary basis. Related to Registered Resources in Metered Subsystems.
    @created 28-Dec-2023 8:22:10 PM
    """

    def __init__(self) -> None:
        """
        Initialize LoadFollowingOperatorInput object.
        """
        self.data_entry_time_stamp: DateTime = DateTime()  # Time the data entry was performed
        self.temp_load_following_down_manual_cap: float = 0.0  # Temporarily manually entered LFD capacity
        self.temp_load_following_up_manual_cap: float = 0.0  # Temporarily manually entered LFU capacity
        self.update_time_stamp: DateTime = DateTime()
        self.update_type: Optional[MQSCHGType] = MQSCHGType.ADD
        self.update_user: str = ""
        self.registered_resource: Optional[RegisteredResource] = RegisteredResource()

