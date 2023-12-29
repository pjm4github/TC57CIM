# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106 on Fri Dec 29 11:15:55 2023
from datetime import datetime
from typing import Optional

from IEC61970.Base.Domain.DateTime import DateTime
from IEC62325.MarketCommon.RegisteredResource import RegisteredResource
from IEC62325.MarketOperations.MarketSystem.MarketResults.InstructionClearing import InstructionClearing
from IEC62325.MarketOperations.ReferenceData.AggregateNode import AggregateNode


class Instructions:
    """
    Provides the necessary information (on a resource basis) to capture the
    Startup/Shutdown instruction results. This information is relevant to the DA
    Market (RUC only) as well as the RT Market (HASP, Pre-dispatch, and Interval).
    """

    def __init__(self) -> None:
        self.binding_dod: float = 0.0
        self.binding_dot: float = 0.0
        self.binding_instruction: str = ""
        self.instruction_cost: float = 0.0
        self.instruction_source: str = ""
        self.instruction_start_time: DateTime = DateTime()
        self.instruction_type: str = ""
        self.manually_blocked: str = ""
        self.min_status_change_time: str = ""
        self.update_time_stamp: DateTime = DateTime()
        self.update_type: str = ""
        self.update_user: str = ""
        # Assuming the types InstructionClearing, AggregateNode, and RegisteredResource are classes
        self.instruction_clearing: Optional[InstructionClearing] = InstructionClearing()
        self.aggregate_node: Optional[AggregateNode] = AggregateNode()
        self.registered_resource: Optional[RegisteredResource] = RegisteredResource()
